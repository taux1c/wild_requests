from setuptools import setup,find_packages

setup(
    name='wild_requests',
    version='0.0.3',
    packages=find_packages(),
    url='https://github.com/taux1c/wild_requests',
    author='Taux1c',
    install_requires=['httpx~=0.25.0'],
    description='Just a module that provides some tools for downloading.',
    long_description="""Wild Requests is a versatile Python package designed to simplify HTTP requests using the powerful HTTPX library. With an intuitive interface and prebuilt logic, it streamlines the process of making web requests, making it an ideal choice for both beginners and experienced developers. Wild Requests supports various HTTP methods, handles authentication, and manages cookies effortlessly. Whether you're building web scrapers, API clients, or need to access web resources, Wild Requests offers a convenient and efficient solution.""",
    long_description_content_type='text/x-rst'
)
