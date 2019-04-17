from requests_html import HTMLSession
import time
import sys

session = HTMLSession()

pages = 1

nxt = "https://old.reddit.com/r/ShrugLifeSyndicate/"

follow_posts = True

while pages <= 10:
  r = session.get(nxt)
  
  articles = r.html.find("article")
  
  titles = r.html.find(".title")
  
  for t in titles:
    title = t.text
    url = t.attrs.get("href")
    if url:
      print(t.text)
  
      if (follow_posts):
        r = session.get("https://old.reddit.com/" + url)
        body = r.html.find(".usertext-body")
        # the first usertext-body is the sidebar
        if len(body) > 1:
          print(body[1].text)
        comments = r.html.find(".comment")
        for c in comments:
          author = c.attrs.get("data-author")
          if author == "AutoModerator":
            continue
          else:
            comment = c.find(".md")
            comment_str = ""
            for l in comment:
              comment_str += l.text + " "
            if author and comment_str:
              print(comment_str, end=" ")
      print("")
      time.sleep(0.1)

  nxt = r.html.find(".next-button")[0]
  nxt = nxt.find("span")[0]
  nxt = list(nxt.absolute_links)[0]
  pages += 1
