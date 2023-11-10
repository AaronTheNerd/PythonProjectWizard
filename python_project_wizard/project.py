from dataclasses import dataclass, field


@dataclass
class Project:
    name: str = field(init=False)
    python_version: str = field(init=False)
    use_black_formatting: bool = field(init=False)
    use_logging: bool = field(init=False)
    use_unittest: bool = field(init=False)
    use_configs: bool = field(init=False)
    use_args: bool = field(init=False)
