import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image


def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            Part.from_image(Image.load_from_file("bouquet_image.jpeg")),
            "generate birthday wishes based on the image",
        ]
    )

    return response.text

# --------  Important: Variable declaration  --------

project_id = "qwiklabs-gcp-00-beb6416b858c"
location = "us-east4"

#  --------   Call the Function  --------
response = generate_text(project_id, location)
print(response)
