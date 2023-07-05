from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open('index.html') as html_file:
            html_code = html_file.read()
        return f"""{html_code}"""

    def __get_article_content(self, page_address):
        pass

    def __get_blog_article(self, page_address):
        return f"""
        <html><head><title>Blog</title></head><body>
        <a href="/">Back</a><br>
        <p>{self.__get_article_content(page_address)}</p>
        </body>
        </html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('page')
        page_content = self.__get_index()
        if page_address:
            page_content = self.__get_blog_article(page_address[0])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


