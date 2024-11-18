class Marca:
    def _init_(self, nombre: str) -> None:
        self._nombre = nombre

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre