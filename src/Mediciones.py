import time 
from functools import wraps
from typing import Any

class Mediciones:

    @staticmethod
    def medir_tiempo(func):
    
            @wraps(func)
            def wrapper(*args, **kwargs) -> tuple[float, Any]:
                  inicio: float = time.perf_counter()
                  resultado: Any = func(*args, **kwargs)
                  fin: float = time.perf_counter()

                  tiempo: float = fin - inicio
                  return (tiempo, resultado)
            
            return wrapper