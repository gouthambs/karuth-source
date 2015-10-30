from pelican import signals
from pelican.contents import Article
from pelican.utils import memoized
from pelican.generators import ArticlesGenerator
from jinja2 import Template

def process_post(article_generator):
    articles = article_generator.articles
    for i, article in enumerate(articles):
        if "templated" in article.metadata.keys() and article.metadata["templated"].lower() == "true":
            template = Template(article.content)
            content = template.render(articles=articles, 
                dates=article_generator.dates, 
                drafts=article_generator.drafts, 
                tags=article_generator.tags, 
                categories=article_generator.categories)
            articles[i] = Article(content, article.metadata, article.settings, article.source_path, article._context)

            
def process(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            process_post(generator)

    
def register():
    signals.article_generator_finalized.connect(process_post)
    