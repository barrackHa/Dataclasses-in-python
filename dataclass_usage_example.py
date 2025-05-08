from dataclasses import dataclass
import logging

# Configure logger to output to stdout
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@dataclass 
class Lendbuzz:
    location: str
    mode: str
    mission: str
    contact: str
        
    def is_hiring (self) -> bool:
        return True
    
    def role_description(self) -> None:
        logger.info("We're hiring a Senior Backend Engineer to help build the future of FinTech.")
        logger.info("You'll join our growing TLV R&D team and shape the backend architecture of our core product.") 
        logger.debug ("Great ping pong skills are a must!")
    
    def requirements(self) -> dict[str, str | bool | int]:
        return {
            "experience_years": 5,
            "Language": "Python",
            "database": "PostgreSQL",
            "APIs": True,
            "microservices": "Advantage",
            "degree": "BSc in CS or equivalent",
        }
    
if __name__ == "__main__":
    location = "Tel Aviv"
    mode = "Hybrid"
    mission = "Reinvent credit access for the underserved"
    contact = "<email>" 
    lendbuzz = Lendbuzz(location, mode, mission, contact)
    if lendbuzz.is_hiring():
        lendbuzz.role_description()
        logger.info(f"Required skills:, {lendbuzz.requirements()}")
        logger.info(f"Apply now or email me directly at: {lendbuzz.contact}")
