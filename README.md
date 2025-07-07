# 🖼️ Agentic Workflow for Text-to-Image Story Illustration

## 📖 Overview
This project proposes an agentic workflow to process and analyze textual content (short stories) and generate consistent, vivid, high-quality illustrations. The system combines state-of-the-art large language models (LLMs), vision-language models, and text-to-image diffusion models into a cohesive pipeline.

**The workflow consists of three main agents:**

- Event Extractor – Summarizes the story and extracts key events with rich contextual details.

- Prompt Refiner – Optimizes prompts to maximize semantic representation in generated images.

- Illustrator – Generates visually appealing and consistent illustrations.

**Two additional tools are integrated:**

- Event Evaluator – Validates the semantic relevance and coverage of extracted events.

- Image Evaluator – Benchmarks character and scene consistency in generated images.


## 🏗️ System Architecture

### 📌 Agents

- Event Extractor

  - Uses a prompt-engineered LLM to extract main events from the text, focusing on locations, characters, actions, and descriptive details.

  - Ensures events span the narrative without overemphasis on specific segments.
    
  - Uses advanced prompt engineering:

      - Role-based prompting (domain expertise as literary analyst).
        
      - Chain-of-Thought prompting (5-step reasoning chain).
        
      - Few-shot examples (positive & negative).
        
      - Retrieval-augmented grounding (attention steering).
        
      - Structured output format for seamless agent communication.

- Prompt Refiner

  - Employs iterative refinement via in-context learning.

  - Produces optimized prompts tailored for text-to-image models.
 
  - Process:

    - Generate multiple variations of the initial prompt.
    
    - Use Stable Diffusion XL to create images for each variation.
    
    - Score each image-prompt pair using CLIP & DSG (Davidsonian Scene Graph).
    
    - Select the best prompt for the next iteration.

  - Techniques:

    - In-Context Learning: Leverages history of past prompts & scores.
    
    - Self-consistent prompting: Evaluates multiple variations for robustness.

  - Logging: Saves best prompts & scores per iteration.

- Illustrator

  - Generates images with emphasis on consistency across scenes.

  - Follows an improved version of prior consistency approaches.

### 🛠️ Tools

- Event Evaluator – Checks extracted events for semantic consistency.

    - SBERT Cosine: Measures semantic similarity between story & events.
    - BERTScore (F1): Fine-grained token-level alignment.
    - ROUGE-L: Surface-level coverage of the original narrative.
    - METEOR: Linguistic relevance & fluency.
    - Relevance Spread: Evaluates distribution of extracted events.
  
- Image Evaluator – Uses a custom benchmark for character and scene consistency.
    - CLIP Embeddings: Semantic consistency across illustrations.
    - DINO Embeddings: Visual coherence of characters.
    - Wasserstein Distance: Color distribution similarity between images.

## Models Used

- **1. LLaMA 3.1 8B-Instruct**
    - Role: Event Extraction & Prompt Refinement

    - Tuned using SFT + RLHF for strong instruction following.

    - Supports context size up to 128k tokens – ideal for full story processing.

    - Lightweight (8B params) and performant with Grouped Query Attention (GQA).

- **2. CLIP (clip-vit-base-patch32)**
    - Role: Image-text alignment for evaluation.

    - Uses contrastive learning to encode text and images into a shared embedding space.

    - Chosen for its balance of performance and computational efficiency.

- **3. BLIP (salesforce/blip-vqa-base)**
    - Role: Visual Question Answering (VQA) for Image Evaluation.

    - Utilizes CapFilt bootstrapping for improved caption generation and filtering.

    - Supports multimodal tasks like retrieval, captioning, and VQA.

- **4. Stable Diffusion XL (stabilityai/stable-diffusion-xl-base-1.0)**
    - Role: Text-to-Image Generation.

    - Based on Latent Diffusion Models with dual text encoders (OpenCLIP-ViT/G & CLIP-ViT/L).

    - Used only the base model due to resource constraints, but still achieves excellent visual quality.

- **5. DINO (facebook/dino-vitb16)**
    - Role: Capturing visual features for evaluating attention consistency in images.

    - Self-supervised vision transformer using student-teacher networks.

    - Produces rich attention maps for understanding visual feature coverage.
 
