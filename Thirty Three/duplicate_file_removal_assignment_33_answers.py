"""
Marvellous Infosystems - Python Automation Assignment 33
Duplicate File Removal Automation Using Python

This single .py file contains the complete solution in the same sequence
as the assignment requirements.

Required package:
    Python standard library only.

Command:
    python duplicate_file_removal_assignment_33_answers.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Example:
    python duplicate_file_removal_assignment_33_answers.py "E:/Data/Demo" 50 marvellousinfosystem@gmail.com

Help:
    python duplicate_file_removal_assignment_33_answers.py --help

Usage:
    python duplicate_file_removal_assignment_33_answers.py --usage

Email configuration:
    Set these environment variables securely before running:
        SMTP_HOST
        SMTP_PORT       (default: 587)
        SMTP_USER
        SMTP_PASSWORD

No email password is hard-coded in this source file.
"""

# ============================================================
# QUESTION / REQUIREMENT 1
# Accept an absolute directory path and recursively scan it.
# ============================================================

import argparse
import hashlib
import logging
import os
import smtplib
import sys
import time
from collections import defaultdict
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path


SCRIPT_NAME = "DuplicateFileRemoval.py"
LOG_DIRECTORY_NAME = "Marvellous"
HASH_ALGORITHM = "sha256"
CHUNK_SIZE = 1024 * 1024


def validate_directory(directory_path):
    """Validate the supplied directory before any file operation."""
    if not directory_path:
        raise ValueError("Directory path is required.")

    path = Path(directory_path).expanduser()

    if not path.is_absolute():
        raise ValueError("Directory path must be an absolute path.")

    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path}")

    if not os.access(path, os.R_OK | os.X_OK):
        raise PermissionError(f"Directory is not accessible: {path}")

    return path.resolve()


def validate_interval(interval_text):
    """Validate that the interval is numeric and greater than zero."""
    if interval_text is None or str(interval_text).strip() == "":
        raise ValueError("Time interval is required.")

    try:
        interval = float(interval_text)
    except (TypeError, ValueError) as exc:
        raise ValueError("Time interval must be numeric.") from exc

    if interval <= 0:
        raise ValueError("Time interval must be greater than zero.")

    return interval


def validate_email(email_address):
    """Perform basic receiver email validation."""
    if not email_address:
        raise ValueError("Receiver email address is required.")

    email = email_address.strip()

    if (
        "@" not in email
        or email.startswith("@")
        or email.endswith("@")
        or "." not in email.rsplit("@", 1)[-1]
    ):
        raise ValueError(f"Invalid email address: {email}")

    return email


# ============================================================
# QUESTION / REQUIREMENT 2
# Identify duplicate files using file checksums.
# ============================================================

def calculate_checksum(file_path):
    """
    Calculate SHA-256 checksum from file content.

    The file is read in chunks so large files do not have to be loaded
    completely into memory.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File no longer exists: {file_path}")

    if not file_path.is_file():
        raise ValueError(f"Path is not a regular file: {file_path}")

    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File is not readable: {file_path}")

    hasher = hashlib.sha256()

    with file_path.open("rb") as file_handle:
        while True:
            chunk = file_handle.read(CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


def scan_files(directory_path, logger):
    """Recursively scan regular files and group them by checksum."""
    checksum_groups = defaultdict(list)
    total_files = 0
    errors = []

    for root, directories, filenames in os.walk(directory_path):
        # Keep traversal deterministic so the first encountered file is
        # consistently preserved within a duplicate group.
        directories.sort()
        filenames.sort()

        for filename in filenames:
            file_path = Path(root) / filename

            try:
                if not file_path.is_file():
                    continue

                total_files += 1
                checksum = calculate_checksum(file_path)
                checksum_groups[checksum].append(file_path)

            except (PermissionError, FileNotFoundError, OSError) as exc:
                message = f"Unable to process {file_path}: {exc}"
                errors.append(message)
                logger.error(message)
            except Exception as exc:
                message = f"Unexpected error processing {file_path}: {exc}"
                errors.append(message)
                logger.exception(message)

    return checksum_groups, total_files, errors


def identify_duplicates(checksum_groups):
    """
    Identify duplicate groups.

    The first file in each checksum group is preserved. All remaining
    files in that group are duplicate copies.
    """
    duplicate_groups = {}

    for checksum, files in checksum_groups.items():
        if len(files) > 1:
            duplicate_groups[checksum] = files

    return duplicate_groups


# ============================================================
# QUESTION / REQUIREMENT 3
# Create the Marvellous log directory and timestamped log file.
# ============================================================

def create_log_directory():
    """Create or reuse the Marvellous directory in the current directory."""
    log_directory = Path.cwd() / LOG_DIRECTORY_NAME
    log_directory.mkdir(parents=True, exist_ok=True)
    return log_directory


def create_log_file(log_directory):
    """Create a timestamp-based log file name."""
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    return log_directory / f"DuplicateRemovalLog_{timestamp}.log"


def configure_logger(log_file):
    """Configure file-only logging; operational messages are not printed."""
    logger = logging.getLogger("DuplicateFileRemoval")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(handler)

    return logger


# ============================================================
# QUESTION / REQUIREMENT 4
# Delete duplicate copies and record paths/checksums/errors.
# ============================================================

def delete_duplicates(duplicate_groups, logger):
    """Delete every duplicate except the first file in each group."""
    deleted_files = []
    deletion_errors = []

    for checksum, files in duplicate_groups.items():
        original = files[0]

        logger.info("Duplicate group checksum: %s", checksum)
        logger.info("Preserved original: %s", original)

        for duplicate in files[1:]:
            try:
                if not duplicate.exists():
                    raise FileNotFoundError(
                        f"Duplicate file no longer exists: {duplicate}"
                    )

                if not duplicate.is_file():
                    raise ValueError(
                        f"Duplicate path is not a regular file: {duplicate}"
                    )

                if not os.access(duplicate, os.W_OK):
                    raise PermissionError(
                        f"File is not writable/deletable: {duplicate}"
                    )

                duplicate.unlink()

                deleted_files.append((str(duplicate), checksum))
                logger.info("Deleted duplicate: %s", duplicate)

            except (PermissionError, FileNotFoundError, OSError, ValueError) as exc:
                message = f"Could not delete {duplicate}: {exc}"
                deletion_errors.append(message)
                logger.error(message)
            except Exception as exc:
                message = f"Unexpected deletion error for {duplicate}: {exc}"
                deletion_errors.append(message)
                logger.exception(message)

    return deleted_files, deletion_errors


# ============================================================
# QUESTION / REQUIREMENT 5
# Perform one complete duplicate-removal operation.
# ============================================================

def run_single_operation(directory_path):
    """
    Execute one complete scan/removal cycle and return statistics.

    Required log information:
    - Start time
    - Completion time
    - Scanned directory
    - Files scanned
    - Duplicates found
    - Duplicates deleted
    - Deleted paths
    - Duplicate checksums
    - Errors
    - Email status
    """
    log_directory = create_log_directory()
    log_file = create_log_file(log_directory)
    logger = configure_logger(log_file)

    start_time = datetime.now()

    stats = {
        "start_time": start_time,
        "completion_time": None,
        "directory": str(directory_path),
        "files_scanned": 0,
        "duplicates_found": 0,
        "duplicates_deleted": 0,
        "deleted_files": [],
        "errors": [],
        "email_status": "Not attempted",
        "log_file": str(log_file),
    }

    logger.info("=" * 80)
    logger.info("Duplicate File Removal Operation Started")
    logger.info("Starting time of scanning: %s", start_time.strftime("%d %B %Y, %I:%M:%S %p"))
    logger.info("Directory scanned: %s", directory_path)
    logger.info("Checksum algorithm: %s", HASH_ALGORITHM.upper())

    try:
        checksum_groups, total_files, scan_errors = scan_files(
            directory_path, logger
        )

        stats["files_scanned"] = total_files
        stats["errors"].extend(scan_errors)

        duplicate_groups = identify_duplicates(checksum_groups)

        stats["duplicates_found"] = sum(
            len(files) - 1 for files in duplicate_groups.values()
        )

        logger.info("Total number of files scanned: %d", total_files)
        logger.info(
            "Total number of duplicate files found: %d",
            stats["duplicates_found"],
        )

        deleted_files, deletion_errors = delete_duplicates(
            duplicate_groups, logger
        )

        stats["deleted_files"] = deleted_files
        stats["duplicates_deleted"] = len(deleted_files)
        stats["errors"].extend(deletion_errors)

        logger.info(
            "Total number of duplicate files deleted: %d",
            stats["duplicates_deleted"],
        )

        logger.info("Deleted duplicate file paths and checksums:")
        if deleted_files:
            for file_path, checksum in deleted_files:
                logger.info("Path: %s | Checksum: %s", file_path, checksum)
        else:
            logger.info("No duplicate files were deleted.")

    except Exception as exc:
        message = f"Operation failed: {exc}"
        stats["errors"].append(message)
        logger.exception(message)

    stats["completion_time"] = datetime.now()

    logger.info(
        "Completion time of scanning: %s",
        stats["completion_time"].strftime("%d %B %Y, %I:%M:%S %p"),
    )
    logger.info("Errors encountered: %d", len(stats["errors"]))

    if stats["errors"]:
        for error in stats["errors"]:
            logger.error("Recorded error: %s", error)

    logger.info("Email delivery status: %s", stats["email_status"])
    logger.info("Duplicate File Removal Operation Completed")
    logger.info("=" * 80)

    for handler in logger.handlers[:]:
        handler.flush()
        handler.close()
        logger.removeHandler(handler)

    return stats


# ============================================================
# QUESTION / REQUIREMENT 6
# Generate required email body and send log as attachment.
# ============================================================

def build_email_body(stats):
    """Build the email body required by the assignment."""
    start = stats["start_time"].strftime("%d %B %Y, %I:%M:%S %p")
    completion = stats["completion_time"].strftime(
        "%d %B %Y, %I:%M:%S %p"
    )

    return f"""Hello,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning: {start}
Completion time of scanning: {completion}
Directory scanned: {stats["directory"]}
Total number of files scanned: {stats["files_scanned"]}
Total number of duplicate files found: {stats["duplicates_found"]}
Total number of duplicate files deleted: {stats["duplicates_deleted"]}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
"""


def send_email(stats, receiver_email):
    """
    Send the operation report and log attachment.

    SMTP credentials are loaded from environment variables rather than
    being hard-coded.
    """
    receiver_email = validate_email(receiver_email)

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port_text = os.getenv("SMTP_PORT", "587")
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    if not smtp_host:
        raise ValueError("SMTP_HOST is not configured.")

    if not smtp_user:
        raise ValueError("SMTP_USER is not configured.")

    if not smtp_password:
        raise ValueError("SMTP_PASSWORD is not configured.")

    try:
        smtp_port = int(smtp_port_text)
    except ValueError as exc:
        raise ValueError("SMTP_PORT must be numeric.") from exc

    message = EmailMessage()
    message["Subject"] = "Duplicate File Removal Operation Report"
    message["From"] = smtp_user
    message["To"] = receiver_email
    message.set_content(build_email_body(stats))

    log_path = Path(stats["log_file"])
    message.add_attachment(
        log_path.read_bytes(),
        maintype="text",
        subtype="plain",
        filename=log_path.name,
    )

    if smtp_port == 465:
        with smtplib.SMTP_SSL(
            smtp_host, smtp_port, timeout=30
        ) as smtp:
            smtp.login(smtp_user, smtp_password)
            smtp.send_message(message)
    else:
        with smtplib.SMTP(
            smtp_host, smtp_port, timeout=30
        ) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(smtp_user, smtp_password)
            smtp.send_message(message)


def record_email_status(stats, receiver_email):
    """Send the email and update the generated log file with its status."""
    log_path = Path(stats["log_file"])

    try:
        send_email(stats, receiver_email)
        stats["email_status"] = (
            f"Email sent successfully to {receiver_email}"
        )
    except (smtplib.SMTPException, OSError, ValueError) as exc:
        stats["email_status"] = f"Email failed: {exc}"
    except Exception as exc:
        stats["email_status"] = f"Unexpected email error: {exc}"

    # Append final email status to the same log file.
    logger = configure_logger(log_path)
    logger.info("Email delivery status: %s", stats["email_status"])

    for handler in logger.handlers[:]:
        handler.flush()
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# QUESTION / REQUIREMENT 7
# Periodic execution until manually terminated.
# ============================================================

def run_periodically(directory_path, interval_minutes, receiver_email):
    """Run the operation repeatedly after the specified interval."""
    interval_seconds = interval_minutes * 60

    while True:
        stats = run_single_operation(directory_path)
        record_email_status(stats, receiver_email)

        # The assignment requires continued execution until manually
        # terminated. Waiting here does not print an operational message.
        try:
            time.sleep(interval_seconds)
        except KeyboardInterrupt:
            # Record termination in a dedicated log instead of printing.
            log_directory = create_log_directory()
            stop_log = log_directory / "DuplicateRemoval_Stop.log"
            logger = configure_logger(stop_log)
            logger.info(
                "Automation manually terminated by the user."
            )
            for handler in logger.handlers[:]:
                handler.flush()
                handler.close()
                logger.removeHandler(handler)
            break


# ============================================================
# QUESTION / REQUIREMENT 8
# Command-line Help and Usage options.
# ============================================================

USAGE_TEXT = """
Usage:
    python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Example:
    python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

Arguments:
    AbsoluteDirectoryPath       Absolute directory to scan recursively.
    TimeIntervalInMinutes       Positive numeric interval in minutes.
    ReceiverEmailAddress        Email address for operation reports.

Options:
    -h, --help                  Show help information.
    -u, --usage                 Show usage information.

SMTP environment variables:
    SMTP_HOST                   SMTP server host.
    SMTP_PORT                   SMTP port; default is 587.
    SMTP_USER                   Sender email/login.
    SMTP_PASSWORD               Sender password or application password.
"""


def build_argument_parser():
    """Build command-line parser with help and usage options."""
    parser = argparse.ArgumentParser(
        prog=SCRIPT_NAME,
        description=(
            "Duplicate File Removal Automation: recursively scans a "
            "directory, identifies duplicates using SHA-256 checksums, "
            "deletes duplicate copies, creates a detailed log and "
            "sends the log by email."
        ),
        epilog=USAGE_TEXT,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "directory",
        nargs="?",
        help="Absolute directory path to scan.",
    )
    parser.add_argument(
        "interval",
        nargs="?",
        help="Positive time interval in minutes.",
    )
    parser.add_argument(
        "receiver_email",
        nargs="?",
        help="Receiver email address.",
    )
    parser.add_argument(
        "-u",
        "--usage",
        action="store_true",
        help="Display usage information.",
    )

    return parser


# ============================================================
# QUESTION / REQUIREMENT 9
# Validate command-line arguments before operation.
# ============================================================

def validate_command_line_arguments(args):
    """Validate all required command-line inputs."""
    if args.usage:
        return None

    missing = []

    if not args.directory:
        missing.append("directory")

    if not args.interval:
        missing.append("time interval")

    if not args.receiver_email:
        missing.append("receiver email")

    if missing:
        raise ValueError(
            "Missing required command-line argument(s): "
            + ", ".join(missing)
        )

    directory = validate_directory(args.directory)
    interval = validate_interval(args.interval)
    email = validate_email(args.receiver_email)

    return directory, interval, email


# ============================================================
# QUESTION / REQUIREMENT 10
# Main program and expected workflow.
# ============================================================

def main():
    """Program entry point."""
    parser = build_argument_parser()
    args = parser.parse_args()

    # --usage is intentionally displayed because it is an explicit
    # documentation option, not an operational status message.
    if args.usage:
        print(USAGE_TEXT.strip())
        return 0

    try:
        validated = validate_command_line_arguments(args)

        if validated is None:
            return 0

        directory, interval, receiver_email = validated

        # The normal operation itself writes all operational information
        # into log files. No progress messages are printed to the console.
        run_periodically(
            directory,
            interval,
            receiver_email,
        )

        return 0

    except (ValueError, FileNotFoundError, NotADirectoryError, PermissionError) as exc:
        # Required operational/error information belongs in a log file.
        try:
            log_directory = create_log_directory()
            error_log = log_directory / "DuplicateRemoval_StartupErrors.log"
            logger = configure_logger(error_log)
            logger.error("Startup validation failed: %s", exc)
            for handler in logger.handlers[:]:
                handler.flush()
                handler.close()
                logger.removeHandler(handler)
        except Exception:
            # Do not expose operational messages on the console.
            pass

        return 1

    except Exception as exc:
        try:
            log_directory = create_log_directory()
            error_log = log_directory / "DuplicateRemoval_StartupErrors.log"
            logger = configure_logger(error_log)
            logger.exception("Unexpected startup failure: %s", exc)
            for handler in logger.handlers[:]:
                handler.flush()
                handler.close()
                logger.removeHandler(handler)
        except Exception:
            pass

        return 1


if __name__ == "__main__":
    sys.exit(main())


# ============================================================
# ASSIGNMENT CHECKLIST
# ============================================================
#
# 1. Accept absolute directory path              -> implemented
# 2. Recursive checksum-based duplicate search   -> implemented
# 3. Keep first duplicate / delete remaining     -> implemented
# 4. Create Marvellous log directory             -> implemented
# 5. Timestamp-based log file                    -> implemented
# 6. Record required operation statistics        -> implemented
# 7. Periodic execution in minutes               -> implemented
# 8. Email with statistics + log attachment      -> implemented
# 9. Help and Usage options                      -> implemented
# 10. Directory/interval/email validation        -> implemented
# 11. File existence/read/delete error handling  -> implemented
# 12. Secure SMTP credentials via environment    -> implemented
# 13. Operational messages stored in log files   -> implemented
# 14. Modular functions with documentation       -> implemented
#
# IMPORTANT SAFETY NOTE:
# This program permanently deletes duplicate files. Test it first on
# a sample directory, as required by the assignment.
