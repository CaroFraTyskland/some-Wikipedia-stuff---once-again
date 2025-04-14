import reference


def __get_default_sort_text(article_name):
    text = reference.replace_letters(article_name)
    text = text.replace("-", "")

    return text


def get_default_sort(article_name):
    sort_name = __get_default_sort_text(article_name)

    return "{{SORTIERUNG:" + sort_name + "}}"


def needs_default_sort(article_name):
    return not (article_name == __get_default_sort_text(article_name))
