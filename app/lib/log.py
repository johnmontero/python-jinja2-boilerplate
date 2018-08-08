# -*- coding: utf-8 -*-

import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout, 
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

