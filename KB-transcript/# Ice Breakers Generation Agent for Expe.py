# Ice Breakers Generation Agent for Expert Persona

# Objective:
# To create personalized ice breakers targeting an expert persona, leveraging detailed analysis of their LinkedIn profile.
# These ice breakers aim to initiate meaningful conversations by highlighting professional admiration, shared interests, and potential collaboration opportunities.

# Input:
# LinkedIn Profile Data (Structured as JSON for ease of processing):
linkedin_profile_data = {
    "full_name": "Full Name",
    "introduction": "Introduction Text",
    "projects": ["Project 1", "Project 2"],
    "experience": [{"company": "Company A", "role": "Role A"}, {"company": "Company B", "role": "Role B"}],
    "topics_of_interest": ["Topic 1", "Topic 2"],
    "communication_style": "Formal/Informal",
}

# Persona:
# The expert persona is a personification of a highly experienced professional recognized for their contributions to their field.
# This persona is characterized by deep knowledge, significant achievements, and a network of professional connections.

# Ice Breaker Generation Logic:

# 1. Professional Admiration:
# Highlight the individual's professional achievements or contributions to their field.
admiration_ice_breaker = f"I've been following your work on {linkedin_profile_data['projects'][0]}, and I'm truly impressed by your innovative approach."

# 2. Shared Interests:
# Identify common grounds based on the topics of interest listed in the profile.
shared_interest_ice_breaker = f"I noticed we share a passion for {linkedin_profile_data['topics_of_interest'][0]}. Have you come across any recent developments in this area?"

# 3. Potential Collaboration:
# Suggest a conversation starter that opens up the possibility of future collaboration.
collaboration_ice_breaker = f"Given your expertise in {linkedin_profile_data['experience'][0]['role']} and my interest in similar projects, I believe there's a lot we could discuss about potential collaboration opportunities."

# Output:
# A JSON dictionary containing personalized ice breakers tailored to the expert persona.
ice_breakers_output = {
    "professional_admiration": admiration_ice_breaker,
    "shared_interests": shared_interest_ice_breaker,
    "potential_collaboration": collaboration_ice_breaker,
}

# Display the generated ice breakers.
print("Generated Ice Breakers:")
for key, value in ice_breakers_output.items():
    print(f"{key.title().replace('_', ' ')}: {value}")
