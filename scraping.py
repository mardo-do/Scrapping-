import requests
from bs4 import BeautifulSoup
import csv

url = "https://lenouvelliste.com/"
response = requests.get(url)
if response.status_code == 200:
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Titre', 'Description', 'Lien', 'Image SRC']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Écrire l'en-tête dans le fichier CSV
    writer.writeheader()
    print("bravo")


    featuredArticle = soup.find_all("div", class_="lnv-featured-article-lg")
    for InvFeat in featuredArticle:
      
      title = InvFeat.find("h1").text.strip()

          # Description
      description = InvFeat.find("p").text.strip()

          # Lien
      link = InvFeat.find("a")["href"]

          # Image (src de la balise img)
      image_src = InvFeat.find("img")["src"]

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})





    print("\n\n\n\n\n")
    print("*" * 50)
    featuredArticle = soup.find_all("div", class_="lnv-featured-article-sm")
    for InvFeat in featuredArticle:
      
      title = InvFeat.find("h1").text.strip()

          # Description
      description = InvFeat.find("p").text.strip()

          # Lien
      link = InvFeat.find("a")["href"]

          # Image (src de la balise img)
      image_src = InvFeat.find("img")["src"]

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})



    print("\n\n\n\n\n")
    print("*" * 50)
    featuredArticle = soup.find_all("div", class_="img-div")

    for InvFeat in featuredArticle:
      # Titre
      title_tag = InvFeat.find("h1")
      title = title_tag.text.strip() if title_tag else "Titre non trouvé"

      # Description
      description_tag = InvFeat.find("p")
      if description_tag:
        description = description_tag.text.strip()
      else:
        description = "Description non trouvée" 

      # Lien
      link_tag = InvFeat.find("a")
      link = link_tag["href"] if link_tag else "Lien non trouvé"

      # Image (src de la balise img)
      image_tag = InvFeat.find("img")
      image_src = image_tag["src"] if image_tag else "Image non trouvée"

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})



    print("\n\n\n\n\n")
    print("*" * 50)
    featuredArticle = soup.find_all("div", class_="lnv-alaminute")
    for InvFeat in featuredArticle:
      
      title = InvFeat.find("h1").text.strip()

          # Description
      if InvFeat.find("p"):
        description = InvFeat.find("p").text.strip()
      else:
        description = "Description non trouvée" 

          # Lien
      link = InvFeat.find("a")["href"]

          # Image (src de la balise img)
      if InvFeat.find("img"):
        image_src = InvFeat.find("img")["src"]
      else:
        image_src = "image non trouvée" 

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})


    print("\n\n\n\n\n")
    print("*" * 50)
    featuredArticle = soup.find_all("div", class_="lnv-most-read-list")
    for InvFeat in featuredArticle:
      if InvFeat.find("h1"):
        title = InvFeat.find("h1").text.strip()
      else:
        title = "titre non trouvée" 

          # Description
      if InvFeat.find("p"):
        description = InvFeat.find("p").text.strip()
      else:
        description = "Description non trouvée" 

          # Lien
      link = InvFeat.find("a")["href"]

          # Image (src de la balise img)
      if InvFeat.find("img"):
        image_src = InvFeat.find("img")["src"]
      else:
        image_src = "image non trouvée" 

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})




    print("\n\n\n\n\n")
    print("*" * 50)
    featuredArticle = soup.find_all("div", class_="lnv-recent-article")
    for InvFeat in featuredArticle:
      if InvFeat.find("h1"):
        title = InvFeat.find("h1").text.strip()
      else:
        title = "titre non trouvée" 

          # Description
      if InvFeat.find("p"):
        description = InvFeat.find("p").text.strip()
      else:
        description = "Description non trouvée" 

          # Lien
      if InvFeat.find("a"):
        link = InvFeat.find("a")["href"]
      else:
        link = "lien non trouvée" 
        
          # Image (src de la balise img)
      if InvFeat.find("img"):
        image_src = InvFeat.find("img")["src"]
      else:
        image_src = "image non trouvée" 

      # Affichage des informations
      print("Titre:", title)
      print("Description:", description)
      print("Lien:", link)
      print("Image SRC:", image_src)
      print("-" * 50)
      # Écrire dans le fichier CSV
      writer.writerow({'Titre': title, 'Description': description, 'Lien': link, 'Image SRC': image_src})










