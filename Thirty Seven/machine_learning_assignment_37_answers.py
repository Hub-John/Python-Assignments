"""
Marvellous Infosystems - Machine Learning Assignment 37
All 10 questions answered in the same sequence as the PDF.
"""

# Q1: Define Artificial Intelligence and compare it with traditional software.
print("""
Q1. Artificial Intelligence (AI)
AI is the field of computer science concerned with creating systems that
can perform tasks associated with human intelligence, such as learning,
reasoning, pattern recognition, language understanding and decision-making.

Traditional software generally follows explicitly programmed rules:
Input -> Fixed Rules -> Output

AI systems can use data, models and learned patterns:
Input + Data/Model -> Intelligent Processing -> Output

Traditional programs normally require rules to be explicitly specified,
whereas many AI systems can learn patterns or make decisions from data.
""")

# Q2: Narrow AI, General AI and Super AI.
print("""
Q2. Three types of AI based on capability

1. Narrow AI:
   Designed for a specific task or limited set of tasks.
   Example: a movie recommendation system.

2. General AI:
   A theoretical AI that could understand, learn and perform a broad
   range of intellectual tasks at a human-like level. It has not been
   achieved.

3. Super AI:
   A hypothetical AI that would exceed human intelligence across
   essentially all intellectual tasks. It remains theoretical.
""")

# Q3: Relationship between AI and ML.
print("""
Q3. Relationship between AI and Machine Learning

Machine Learning is a PART OF Artificial Intelligence.

Hierarchy:

Artificial Intelligence (AI)
|
+-- Machine Learning (ML)
|   |
|   +-- Deep Learning (DL)
|
+-- Other AI approaches
    (rule-based systems, search, planning, etc.)

AI is the broader field. ML is an approach within AI that learns patterns
from data. Deep Learning is a subset of ML based on multi-layer neural
networks.
""")

# Q4: Define ML and explain supervised, unsupervised and reinforcement learning.
print("""
Q4. Machine Learning and its three main types

Machine Learning (ML) is a branch of AI in which systems learn patterns
from data and use those patterns to make predictions, decisions or
discover useful structure without requiring a separate explicit rule
for every case.

1. Supervised Learning:
   Learns from labelled input-output examples.
   Example: classifying an email as spam or not spam.

2. Unsupervised Learning:
   Learns from mainly unlabelled data and discovers patterns or groups.
   Example: customer segmentation using clustering.

3. Reinforcement Learning:
   An agent learns by interacting with an environment and receiving
   rewards or penalties.
   Example: an agent learning to play a game.
""")

# Q5: Supervised vs Unsupervised.
print("""
Q5. Supervised Learning vs Unsupervised Learning

+-------------------+--------------------------+---------------------------+
| Basis             | Supervised Learning     | Unsupervised Learning     |
+-------------------+--------------------------+---------------------------+
| Data requirement  | Labelled data            | Mainly unlabelled data    |
| Output            | Predicts known target    | Finds hidden structure    |
| Main tasks        | Classification,          | Clustering, association, |
|                   | regression               | dimensionality reduction |
| Applications      | Spam detection,          | Customer segmentation,   |
|                   | price prediction         | pattern discovery        |
+-------------------+--------------------------+---------------------------+

Supervised learning learns a mapping from inputs to known outputs.
Unsupervised learning searches for structure without a target label.
""")

# Q6: Reinforcement Learning.
print("""
Q6. Reinforcement Learning

Reinforcement Learning (RL) is a Machine Learning approach where an agent
interacts with an environment, takes actions and receives rewards or
penalties. It learns a policy that aims to maximize cumulative reward.

Basic cycle:
State -> Action -> Environment -> Reward -> New State

Example: a game-playing agent learns which actions produce better scores.
""")

# Q7: Deep Learning vs traditional ML.
print("""
Q7. Deep Learning

Deep Learning is a subset of Machine Learning that uses neural networks
with multiple layers to learn complex patterns and representations.

Traditional Machine Learning:
- Often uses manually selected or engineered features.
- Commonly works well with structured/tabular data.
- Examples: Decision Tree, Logistic Regression, KNN.

Deep Learning:
- Uses multi-layer neural networks.
- Can automatically learn representations/features from raw data.
- Often useful for images, speech, natural language and other complex data.
- Commonly benefits from large datasets and substantial computation.

Hierarchy: AI -> Machine Learning -> Deep Learning
""")

# Q8: Data Science vs ML.
print("""
Q8. Data Science

Data Science is an interdisciplinary field that uses data, statistics,
programming, visualization, domain knowledge and Machine Learning to
extract insights and support decisions.

Data Science is broader than Machine Learning. It can include data
collection, cleaning, exploration, visualization, statistical analysis,
model building, communication and deployment.

Machine Learning specifically focuses on algorithms that learn patterns
from data for prediction, classification, decision-making or discovery.

Therefore, Machine Learning is an important tool within many Data Science
projects.
""")

# Q9: Data Science lifecycle.
print("""
Q9. Data Science Lifecycle

1. Data Collection
   Gather relevant data from files, databases, APIs, sensors, surveys, etc.

2. Data Cleaning
   Handle missing values, duplicates, incorrect values and inconsistent
   formats.

3. Data Analysis
   Explore data using statistics and visualizations to identify trends,
   relationships and patterns.

4. Model Building
   Select features and suitable algorithms, train models and evaluate them.

5. Deployment
   Put the model/analysis into practical use through an application, API,
   dashboard or business workflow and monitor it.

Lifecycle:
Data Collection -> Data Cleaning -> Data Analysis -> Model Building
-> Deployment
""")

# Q10: Generative AI vs predictive ML.
print("""
Q10. Generative AI (GenAI)

Generative AI is AI that can generate new content based on patterns learned
from training data. It can generate text, images, audio, video or code.

Traditional predictive Machine Learning:
- Usually predicts a class, value, probability or other target.
- Example: predicting whether a student will Pass or Fail.

Generative AI:
- Generates new content.
- Example: generating an explanation, an image from a prompt, or computer
  code.

Simple difference:
Predictive ML -> "What is the likely outcome?"
Generative AI  -> "What new content can be generated?"
""")

print("""
============================================================
ASSIGNMENT 37 COMPLETED
============================================================
All 10 questions have been answered in question-answer sequence.
""")
