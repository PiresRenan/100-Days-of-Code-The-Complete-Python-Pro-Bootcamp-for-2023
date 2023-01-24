# # biblioteca bs4
# from bs4 import BeautifulSoup

# # ALTERNATIVA
# # import lxml
# # soup = BeautifulSoup(contents, "lxml")

# # abrindo o arquivo html a ser analisado
# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()

# # criando o objeto com as info da pag html
# soup = BeautifulSoup(contents, "html.parser")

# # # mostrando o conteudo total do title
# # print(soup.title)
# # # mostrando o nome da tag
# # print(soup.title.name)
# # # mostrando o que ta dentro da tag 
# # print(soup.title.string)
# # # mostrando todo o codigo html 
# # print(soup.prettify())
# # # mostrando a primeira tag "a" ou "li" ou "p" de referência 
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)

# # pegando todas informações de determinada tag, e formatado em lista
# all_anchor_tags = soup.find_all(name="a")
# # capturando determinada parte dentro de diversas tag 
# # for tag in all_anchor_tags:
# #     # pegando o texto em frente a tag 
# #     # print(tag.getText())
# #     # pegando o href 
# #     print(tag.get("href"))
    
# # encontrando itens especificos dentro do html, por id
# heading = soup.find(name="h1", id="name")    
# # print(heading)

# # # encontrando pela classe, prestar atenção no underline depois do class
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # # destrinchando 
# # print(section_heading.get_text())
# # print(section_heading.name)
# # print(section_heading.get("class"))

# # encontrando várias informações pelo nome da classe 
# class_is_heading = soup.find_all(class_="heading")
# # print(class_is_heading)

# h3_heading = soup.find_all("h3", class_="heading")
# # print(h3_heading)

# # usando tags css para encontrar infos 
# company_url = soup.select_one(selector="p a")
# # print(company_url)
# name = soup.select_one(selector="#name")
# # print(name)

# # selecionar todos itens com a mesma nomenclatura css 
# headings = soup.select(".heading")
# print(headings)


############################################################
# PEGANDO INFO DE UMA PAGINA NA WEB
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# article_tag = soup.find(name="a" , class_="titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(f"Informações importantes que podemos tirar analisando um html por Python: "+
#       f"\nNome do artigo numero 1: {article_text}"+
#       f"\nLink para o artigo: {article_link}"+
#       f"\nNumero de votos positivos: {article_upvote}"
#       )

# analisando diversos dentro de um html 
articles = soup.find_all(name="a" , class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# print(f"Informações importantes que podemos tirar analisando um html por Python: "+
#       f"\nNome de todos artigos na página: {article_texts}"+
#       f"\nLinks para todos os artigos: {article_links}"+
#       f"\nNumero de votos positivos: {article_upvotes}"
#       )

highest = max(article_upvotes)
index_highest = article_upvotes.index(highest)

print(f"O artigo mais relevante segundo os votos é: "+
      f"\n--{article_texts[index_highest]}"+
      f"\n--{article_links[index_highest]}"+
      f"\n--{highest}")






















