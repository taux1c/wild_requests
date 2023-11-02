from setuptools import setup,find_packages

setup(
    name='wild_requests',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/taux1c/wild_requests',
    author='Taux1c',
    description='Just a module that provides some tools for downloading.',
    long_description="""Long Description:
-----------------

**wild_requests**: Simplify Your HTTP Requests with Prebuilt Logic

`wild_requests` is a versatile Python module designed to streamline your HTTP requests using the power of HTTPX, a fully featured HTTP client for Python. With `wild_requests`, you can effortlessly make HTTP requests with prebuilt logic and handle common use cases, all while benefiting from the performance and flexibility of HTTPX.

Key Features:
- **Convenient and Lightweight:** `wild_requests` offers a straightforward and lightweight interface for making HTTP requests, allowing you to focus on your application's logic instead of the intricacies of HTTP.

- **Built on HTTPX:** Leverage the robust capabilities of HTTPX, which provides support for asynchronous requests, HTTP/1.1, HTTP/2, WebSocket, and more.

- **Prebuilt Logic:** Save time and effort with prebuilt logic for common HTTP operations, such as GET requests, POST requests, and handling query parameters.

- **Session Management:** Manage sessions and cookies effortlessly for maintaining state across requests.

- **Customization:** While `wild_requests` offers ready-to-use functionality, it's also highly customizable to adapt to your specific use cases and requirements.

- **Asynchronous Support:** Take advantage of asynchronous request handling when working with Python's `asyncio`.

- **Enhanced Performance:** Utilize the inherent performance benefits of HTTPX for efficient HTTP communication.

Whether you're building a web scraper, a REST API client, or any other Python application that relies on HTTP requests, `wild_requests` empowers you to achieve your goals with simplicity and efficiency.

Install `wild_requests` today and enhance your Python HTTP requests with ease.
"""
)
