import http.server
import requests

def getKey():
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
  url = "https://cgerrydlc.ru/Cherry/FREEMODS/LEOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoo56465465656546456rtrythghhgfh676765765767657657hjhgjghjghjghjhgjghjghj6786756756fgh1r.php"
  script = requests.get(url, headers=headers).text
  responsee = requests.get(script.replace("<script>setTimeout(function() { window.location.href='", '').replace("'; }, 1);</script>", ''), headers=headers)
  return responsee.text.split("- ")[1].replace("\n", "")
class RequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    key = getKey()
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100..900&display=swap" rel="stylesheet">
    <title>Ваш ключ</title>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        let buttons = document.querySelectorAll(".button");

        for (var i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener("click", (e) => {
                e.preventDefault();

                let overlay = document.createElement("span");
                overlay.classList.add("overlay");
                e.target.appendChild(overlay);
                const rect = e.target.getBoundingClientRect();
                let xValue = e.clientX - rect.left;
                let yValue = e.clientY - rect.top;

                overlay.style.left = xValue + "px";
                overlay.style.top = yValue + "px";

                overlay.addEventListener("animationend", () => {
                    overlay.remove();
                });
            });
        }
    });
    function copyKey(){
    	navigator.clipboard.writeText(''' + key + '''");
    }
    </script>
    <style>
        body {
            background: black;
        }
        .main {
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            align-items: center;
            height: 100vh;
            color: white;
            font-family: "Montserrat", sans-serif;
        }
        h1, a, button {
            margin: 5px 0;
        }
        .button {
            position: relative;
            display: inline-block;
            background: #2b2b2b;
            font-family: "Montserrat", sans-serif;
            color: white;
            padding: 10px;
            font-weight: 700;
            border-radius: 25px;
            width: 170px;
            border: 3px solid #3b3b3b;
            transition: 0.3s;
            overflow: hidden;
        }
        
        
        .button .overlay {
            position: absolute;
            background: #fff;
            top: 0;
            left: 0;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            animation: blink 0.5s linear;
        }

		@media (hover: hover) {
        	.button:hover {
            	background: #8c8c8c;
            	border: 3px solid #adadad;
            }
        }

        @keyframes blink {
            0% {
                height: 0px;
                width: 0px;
                opacity: 0.3;
            }
            100% {
                height: 400px;
                width: 400px;
                opacity: 0;
            }
        }
        
    </style>
</head>
<body>
    <div class="main">
        <h1>Ваш ключ</h1>
        <a>''' + key + '''</a>
        <button class="button" onclick="copyKey()">Скопировать</button>
    </div>
</body>
</html>''', "utf-8"))


handler = app = RequestHandler
