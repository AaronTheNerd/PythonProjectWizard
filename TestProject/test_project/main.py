from test_project.args import get_argparser
from test_project.configs import load_configs
from test_project.log import enable_logging
import logging



def main():
    # Enable logging
    enable_logging()
    logger = logging.getLogger(__name__)
    
    # Get the argument parser
    parser = get_argparser()
    args = parser.parse_args()
    
    # Read Configs from JSON file
    configs = load_configs()

    
    """Cool stuff here!"""
    ...


if __name__ == "__main__":
    main()
