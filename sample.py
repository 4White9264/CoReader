import _package_CoReader_Poly as CoReader
import json

article = 'Self-Modeling Based Diagnosis of Software-Defined Networks'
article_info = CoReader.get_article_details(article)

print(json.dumps(article_info, indent=4, ensure_ascii=False))