"""
Coherent Item
"""
from pybricks.geometry import Matrix


class CoherentItem:
    """
    A CoherentItem shall describe a vector in :math:`\mathbb{R}³`

    """

    def __init__(self, id: int, name: str, boundary: Matrix):
        """

        Parameters
        ----------
        id : int
            Simple identifier
        name : str
            Friendly name of that coherent object part.
        boundary :
            The vector describing a part of the object.
        """
        self._id: int = id
        self._name: str = name
        self._boundary: Matrix = boundary
        self._is_coherent: bool = False

    @property
    def is_coherent(self) -> bool:
        """

        Returns
        -------
        bool : is_coherent
            True if this object is a coherent object, False otherwise.

        """
        return self._is_coherent

    @is_coherent.setter
    def is_coherent(self, coherent: bool):
        self._is_coherent = coherent

