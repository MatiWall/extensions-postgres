import functools
from contextlib import contextmanager
import psycopg2
import pandas as pd

from .config import get_config, REQUIRED_ARGS


def apply_config(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _kwargs = {**get_config(), **kwargs}
        for arg in _kwargs.keys():
            if arg not in REQUIRED_ARGS:
                raise KeyError(f'Required keyword argument {arg} not specified')
        return func(*args, **_kwargs)

    return wrapper

def gen_apply_config(func):

    @functools.wraps(func)
    def wrapper(**kwargs):
        args = {**get_config(), **kwargs}
        for arg in REQUIRED_ARGS:
            if arg not in args.keys():
                raise KeyError(f'Required keyword argument {arg} not specified')
        for f in func(**args):
            yield f

    return wrapper

@contextmanager
@gen_apply_config
def get_connection(
        **kwargs
):

    # Code to acquire resource, e.g.:
    with psycopg2.connect(**kwargs) as conn:
        yield conn


@contextmanager
@gen_apply_config
def get_cursor(
        **kwargs
):

    # Code to acquire resource, e.g.:
    with psycopg2.connect(**kwargs) as conn:
        with conn.cursor() as cursor:
            yield cursor


@apply_config
def read_sql(sql: str, **kwargs):
    with get_cursor(**kwargs) as cursor:
        # Example: Execute a query and return a DataFrame
        cursor.execute(sql)
        result = cursor.fetchall()
        # Convert result to Pandas DataFrame
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    return df