def format_tags(tags):
    return ','.join(f'"{tag.replace("_", " ")}"' for tag in tags)


def format_filename(date, title):
    return f'{date}-{title.replace(" ", "-").lower()}.markdown'


def write_frontmatter(args):
    f = open(f"./_posts/{format_filename(args['date'], args['title'])}", "w")
    f.write("---\n")
    f.write("layout: post\n")
    f.write(f"title: {args['title']}\n")
    f.write(f"date: {args['date'][:10]} {args['date'][11:].replace('-', ':')}\n")
    f.write("comments: true\n")
    f.write("published: true\n")
    f.write("categories: [\"post\"]\n")
    f.write(f"tags: [{format_tags(args['tags'])}]\n")
    f.write(f"author: {args['author']}\n")
    f.write(f"modified_when: {args['modified_when']}\n")
    f.write("---\n")
    f.close()


def write_body(args, body):
    f = open(f"./_posts/{format_filename(args['date'], args['title'])}", "a+")
    f.write(body)
    f.close()


