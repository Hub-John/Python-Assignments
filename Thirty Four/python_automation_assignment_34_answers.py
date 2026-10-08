"""
Marvellous Infosystems - Python Automation Assignment 34
All 4 questions implemented in sequence.
Requires: pip install psutil

Usage:
  python python_automation_assignment_34_answers.py q1
  python python_automation_assignment_34_answers.py q2 Notepad
  python python_automation_assignment_34_answers.py q3 Demo
  python python_automation_assignment_34_answers.py q4 Demo user@example.com

For Q4 set SMTP_HOST, SMTP_PORT, SMTP_USER and SMTP_PASSWORD as environment
variables. No email password is hard-coded in this program.
"""

import argparse, logging, os, smtplib, socket
from pathlib import Path
from email.message import EmailMessage

try:
    import psutil
except ImportError:
    psutil = None


def logger_for(filename):
    """Create file-only logging."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    log = logging.getLogger("assignment34")
    log.setLevel(logging.INFO)
    log.handlers.clear()
    h = logging.FileHandler(path, encoding="utf-8")
    h.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    log.addHandler(h)
    return log


def require_psutil():
    if psutil is None:
        raise RuntimeError("psutil is required. Install it with: pip install psutil")


def running_processes():
    """Return process name, PID and username for running processes."""
    require_psutil()
    result = []
    for proc in psutil.process_iter(["pid", "name", "username"]):
        try:
            info = proc.info
            result.append({
                "name": info.get("name") or "Unknown",
                "pid": info.get("pid"),
                "username": info.get("username") or "Unknown",
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        except Exception:
            continue
    return sorted(result, key=lambda x: (x["name"].lower(), x["pid"] or -1))


def write_process_log(filename, processes, title):
    log = logger_for(filename)
    log.info("=" * 70)
    log.info(title)
    log.info("Computer: %s", socket.gethostname())
    log.info("Total processes: %d", len(processes))
    log.info("%-40s %-10s %-35s", "Process Name", "PID", "Username")
    log.info("-" * 90)
    for item in processes:
        log.info("%-40s %-10s %-35s",
                 item["name"], item["pid"], item["username"])
    log.info("-" * 90)


def validate_directory(name):
    if not name or not name.strip():
        raise ValueError("Directory name cannot be empty.")
    path = Path(name).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")
    return path


def validate_email(address):
    if not address or "@" not in address or "." not in address.rsplit("@", 1)[-1]:
        raise ValueError(f"Invalid email address: {address}")
    return address


# ============================================================
# QUESTION 1
# Display running process name, PID and Username.
# Usage: ProcInfo.py
# ============================================================
def question_1():
    log_file = Path.cwd() / "ProcInfo.log"
    try:
        write_process_log(
            log_file, running_processes(),
            "QUESTION 1 - Running Process Information"
        )
    except Exception as exc:
        logger_for(log_file).exception("Question 1 failed: %s", exc)


# ============================================================
# QUESTION 2
# Accept process name and display its information if running.
# Usage: ProcInfo.py Notepad
# ============================================================
def question_2(process_name):
    log_file = Path.cwd() / "ProcInfo.log"
    try:
        if not process_name.strip():
            raise ValueError("Process name cannot be empty.")
        require_psutil()
        wanted = process_name.lower().strip()
        found = []
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                info = proc.info
                name = info.get("name") or ""
                stem = Path(name).stem
                if name.lower() == wanted or stem.lower() == wanted:
                    found.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        log = logger_for(log_file)
        if not found:
            log.info("Process '%s' is not running.", process_name)
            return
        log.info("QUESTION 2 - Process: %s", process_name)
        for info in found:
            log.info("Process Name: %s", info.get("name") or "Unknown")
            log.info("PID: %s", info.get("pid"))
            log.info("Username: %s", info.get("username") or "Unknown")
    except Exception as exc:
        logger_for(log_file).exception("Question 2 failed: %s", exc)


# ============================================================
# QUESTION 3
# Accept directory and create process log in that directory.
# Usage: ProcInfoLog.py Demo
# ============================================================
def create_process_log(directory):
    directory = validate_directory(directory)
    from datetime import datetime
    filename = directory / (
        "ProcessInfo_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
    )
    write_process_log(
        filename, running_processes(),
        "QUESTION 3 - Running Process Information"
    )
    return filename


def question_3(directory):
    fallback = Path.cwd() / "ProcInfoLog_Error.log"
    try:
        filename = create_process_log(directory)
        logger_for(filename).info("Log created successfully: %s", filename)
    except Exception as exc:
        logger_for(fallback).exception("Question 3 failed: %s", exc)


# ============================================================
# QUESTION 4
# Accept directory and email, create process log and email it.
# Usage: ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
# ============================================================
def send_log(filename, recipient):
    validate_email(recipient)
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")

    if not all([host, user, password]):
        raise ValueError(
            "Set SMTP_HOST, SMTP_PORT, SMTP_USER and SMTP_PASSWORD "
            "environment variables before using Q4."
        )

    msg = EmailMessage()
    msg["Subject"] = "Running Process Information"
    msg["From"] = user
    msg["To"] = recipient
    msg.set_content("Attached is the running process information log.")
    msg.add_attachment(
        Path(filename).read_bytes(),
        maintype="text", subtype="plain",
        filename=Path(filename).name
    )

    if port == 465:
        with smtplib.SMTP_SSL(host, port, timeout=30) as smtp:
            smtp.login(user, password)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(host, port, timeout=30) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(user, password)
            smtp.send_message(msg)


def question_4(directory, recipient):
    fallback = Path.cwd() / "ProcInfoLog_Email_Error.log"
    try:
        filename = create_process_log(directory)
        send_log(filename, recipient)
        logger_for(filename).info("Log emailed successfully to %s", recipient)
    except Exception as exc:
        logger_for(fallback).exception("Question 4 failed: %s", exc)


def main():
    parser = argparse.ArgumentParser(description="Automation Assignment 34")
    sub = parser.add_subparsers(dest="question", required=True)

    sub.add_parser("q1")

    q2 = sub.add_parser("q2")
    q2.add_argument("process_name")

    q3 = sub.add_parser("q3")
    q3.add_argument("directory")

    q4 = sub.add_parser("q4")
    q4.add_argument("directory")
    q4.add_argument("email")

    args = parser.parse_args()

    if args.question == "q1":
        question_1()
    elif args.question == "q2":
        question_2(args.process_name)
    elif args.question == "q3":
        question_3(args.directory)
    elif args.question == "q4":
        question_4(args.directory, args.email)


if __name__ == "__main__":
    main()
