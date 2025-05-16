import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import io
import json

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API"))

def sort_industries(industries=None):
    """Sort industries into predefined groups using Gemini."""
    if not industries:
        return {}
        
    # Convert to set to remove duplicates and filter out None/empty values
    unique_industries = list(set(industry for industry in industries if industry))
    
    if not unique_industries:
        return {}
    
    # Define the predefined categories we want to use
    predefined_categories = [
        "AI & Machine Learning", "Technology", "Finance", "Healthcare", "Education", "Retail", 
        "Manufacturing", "Media", "Consulting", "Real Estate", "Energy",
        "Transportation", "Food & Beverage", "Entertainment", "Fashion",
        "Sports", "Telecommunications", "Legal Services", "Agriculture",
        "Nonprofit", "Other"
    ]
    
    # Create the prompt for Gemini
    prompt = f"""
    I have a list of industries from company outreach data. Please categorize these industries into ONLY the following predefined groups:
    {', '.join(predefined_categories)}
    
    Here's the list of industries to categorize:
    {', '.join(unique_industries)}
    
    Important instructions:
    1. Put all AI, Machine Learning, and Artificial Intelligence related industries into the "AI & Machine Learning" category
    2. Put other technology industries into the "Technology" category
    3. Make sure every industry from my list is included in exactly one category
    4. Do not create any new categories beyond what I've specified
    
    Please return your answer as a JSON object where:
    - Keys are ONLY the category names from my predefined list above
    - Values are arrays of industries from my list that belong to that category
    
    Return ONLY the JSON object with no additional text.
    """
    
    try:
        # Generate content with Gemini
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(prompt)

        # Parse the response as JSON
        result_text = response.text

        print("Raw response from Gemini:")
        print(result_text)
        
        # Clean up the response if it contains markdown code blocks
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()
            
        grouped_industries = json.loads(result_text)
        
        # Ensure all predefined categories exist in the result
        for category in predefined_categories:
            if category not in grouped_industries:
                grouped_industries[category] = []
                
        # Print each category and its industries for verification
        #print("\nCategorized Industries:")
        #for category in predefined_categories:
        #    industries_in_category = grouped_industries.get(category, [])
        #    print(f"\n{category} ({len(industries_in_category)} industries):")
        #    for industry in industries_in_category:
        #        print(f"  - {industry}")
                
        return grouped_industries
        
    except Exception as e:
        print(f"Error grouping industries: {e}")
        # Return empty dictionary with predefined categories if API fails
        return {category: [] for category in predefined_categories}

