# -*- coding: utf-8 -*-
import os
import json
import argparse

from jinja2 import Environment, FileSystemLoader

from lib.log import logger

def define_arguments():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('-f', '--file', type=str, default='report.json',
                        help='Json file')
    return parser.parse_args()

def render_template(template_dir, template_name, **context):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(**context)

def load_json(filename):
    with open(filename) as f:
        return json.loads(f.read())


def main():
    try:
        arguments = define_arguments()
        logger.info('Leyendo archivo : "%s".' % arguments.file)
        filename = "{}".format(arguments.file)

        if os.path.isfile(filename):
            context = { "results": load_json(filename) }
        else:
            context = {}

        logger.info('Generando Report.html')
        html = render_template('./templates', 'report.html', **context)
        with open('report.html', 'w', encoding='utf8', errors="ignore") as f:
            f.write(html)

    except Exception as e:
        logger.error(e, exc_info=True)
        

if __name__ == "__main__":
    main()