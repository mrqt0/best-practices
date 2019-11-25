#!/usr/bin/env python3

from html.parser import HTMLParser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


parser = HTMLParser()

class WebGui(BaseHTTPRequestHandler):

    def do_GET(self):
        # print(self.headers)
        # requestline: "<method> <uri> <version> CRLF"
        # self.requestline == f"{self.command} {self.path} {self.request_version}"

        print("path:", self.path)
        query_string = urlparse(self.path).query
        data = parse_qs(query_string)
        # get path part
        
        # dynamically edit html document: (use html.parser module)
        # - create menu of commands from command list
        # - when connected, show waveform box (waveform and preset)
        # - show connection status
        # - when connected to waveform / waveform already active: show command list
        # - when getting property : show text box

        self.send_response(200)
        with open("webgui.html") as f:
            data = f.read()
            parser.feed(data)
            data = data.replace("FOOBAR", "BEBECHONCITO")
            self.wfile.write(data.encode("utf-8"))

    def handle_connect(self):
        print("Connecting to ''")
        # Finally return new page with connection info

    def do_POST(self):
        pass


def main():
    server = HTTPServer(("", 80), WebGui)
    server.serve_forever()


if __name__ == "__main__":
    main()
