# Extracting Semantic Topics about Development in Africa from Social Media

## Abstract

The extraction of knowledge about prevalent social issues discussed on social media in Africa using Artificial Intelligence (AI) techniques is crucial for informing public governance. Our study has two main goals: (a) to develop machine learning models that identify common topics of social concern related to Africa on social media, and (b) to design a classifier capable of inferring the specific common topic associated with a given social media post.

## Methodology

We implemented a three-step framework for topic identification:

1. **Text Embeddings**: We used text-based representation learning methods to generate embeddings for feature representation.
2. **Topic Modeling**: State-of-the-art Natural Language Processing models, including BERTopic, were employed to organize these representations into groups.
3. **Topic Generation**: Large language models, such as Llama2, were used to generate meaningful short-sentence labels from the bag-of-tokens associated with each group. Additionally, Llama2 helped refine these into single-word themes that describe each topic in relation to social concerns about development.

For the classification goal, we trained classifiers using ensemble voting and stacking learners to infer which of the identified common topics best characterizes a social media post.

## Experiments and Findings

Our experimental study involved the creation of the Social Media for Africa (SMA) corpus, comprising 22,036 records extracted from social media comments on Twitter (X) and YouTube.

- **Topic Modeling**: The BERTopic model identified 304 topics with a coherence score of 0.81 C-v. After merging, BERTopic+ created 11 common topic classes with a coherence score of 0.76 C-v.
- **Theme Extraction**: Llama2 refined the leading token words into 98 unique themes, achieving a C-v score of 0.75 and an IRBO score of 0.50.

We then used the identified topics as labels to train a topic classifier, leveraging Llama2 on the SMA corpus.

### Classifier Performance

- **BERTopic Model**: Achieved 0.83 accuracy and 0.82 F1 score using ensemble voting.
- **BERTopic+ Model**: Achieved the highest accuracy and F1 score of 0.95 with ensemble voting when trained on topic classes.
- **BERTopic_Theme**: Achieved 0.93 accuracy and F1 score with the ensemble voting classifier.

Overall, the ensemble stacking method slightly outperformed voting methods for short sentence topic labeling.

## Policy Implications

For African policymakers, the most pressing social issues identified include:

- COVID-19 restrictions affecting public health and economic recovery.
- Promoting entrepreneurial innovation in energy and environmental sustainability to combat climate change.
- Strategically responding to China's rise in global politics to maintain geopolitical stability and foster international cooperation.

## Keywords

- social concerns
- social media
- semantic topic labels
- themes
- topic modeling
- LLMs
