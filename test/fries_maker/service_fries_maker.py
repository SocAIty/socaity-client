from fastsdk.definitions.ai_model import AIModelDescription
from fastsdk.definitions.enums import ModelDomainTag, ModelTag
from fastsdk.web.service_client import ServiceClient
from fastsdk import MultiModalFile, ImageFile, AudioFile, VideoFile


srvc_fries_maker = ServiceClient(
    service_url="localhost:8000/api",
    model_description=AIModelDescription(
        model_name="FriesMaker",
        model_domain_tags=[ModelDomainTag.IMAGE, ModelDomainTag.AUDIO],
        model_tags=ModelTag.OTHER,
        model_description="This service is used to make fries. This is the test service of the socaity_router."
    )
)
srvc_fries_maker.add_endpoint(endpoint_route="make_fries", post_params={"fries_name": str, "amount": int})
srvc_fries_maker.add_endpoint(
    endpoint_route="make_file_fries",
    file_params={"potato_one": MultiModalFile, "potato_two": MultiModalFile, "potato_three": MultiModalFile}
)
srvc_fries_maker.add_endpoint(endpoint_route="make_image_fries", file_params={"potato_one": ImageFile})
srvc_fries_maker.add_endpoint(endpoint_route="make_audio_fries", file_params={"potato_one": AudioFile, "potato_two": AudioFile})
srvc_fries_maker.add_endpoint(endpoint_route="make_video_fries", file_params={"potato_one": VideoFile, "potato_two": VideoFile})

