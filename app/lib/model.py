from typing import Any, Iterable
from app.lib.table_view import TableView


class Model(TableView):
    """ Base model class for module entities

    """
    def add(self, data: dict, ret: str = 'id', **kwargs: dict) -> Any:
        """ Creates a db entry

        Parameters
        ----------
        data : dict
        ret : str

        Returns
        -------
        Any
            Count of inserted rows if no returning value is specified

        """
        return self.insert(
            self.preprocess(self.before_add(data, **kwargs), **kwargs), ret)

    def edit(self, id: int, data: dict, ret: str = 'id',
             **kwargs: dict) -> Any:
        """ Updates an entry

        Parameters
        ----------
        id : int
        data : dict
        ret : str

        Returns
        -------
        Any
            Count of updated rows if no returning value is specified

        """
        return self.update_by_id(
            self.preprocess(self.before_edit(id, data, **kwargs), **kwargs),
            id, ret)

    def remove(self, id: int) -> int:
        """ Deletes record by provided identifier

        Parameters
        ----------
        id : int
            Count of deleted rows

        """
        self.before_remove(id)
        return self.delete_by_id(id)

    def preprocess(self, data: dict, **kwargs: dict) -> dict:
        return data

    def before_add(self, data: dict, **kwargs: dict) -> dict:
        """ Perform operations before adding a row

        Parameters
        ----------
        data : dict
        **kwargs : dict

        Returns
        -------
        dict

        """
        return data

    def before_edit(self, id: int, data: dict, **kwargs) -> dict:
        """ Perform operations before editing the row

        Parameters
        ----------
        id : int
        data : dict
        **kwargs : dict

        Returns
        -------
        dict

        """
        return data

    def before_remove(self, id: int):
        """ Perform operations before removing the row

        Parameters
        ----------
        id : int

        Returns
        -------
        dict

        """
        pass

    def by_ids(self, ids: list, order_by: str = 'id') -> Iterable:
        """ Selecting records by set of IDs

        Parameters
        ----------
        ids : list
        order_by : str

        Returns
        -------
        Iterable

        """
        # TODO rafactor IN and use ANY. This is prone to SQL INJECTION
        return self.select("id IN ({})".format(", ".join(map(str, ids))),
                           order_by=order_by)

    def by_key(self, values: list, key: str = 'id',
               order_by: str = 'id') -> Iterable:
        """ Selecting records by set of key

        Parameters
        ----------
        values : list
        key : str
        order_by : str

        Returns
        -------
        Iterable

        """
        return self.select("{}::TEXT = ANY (%(vals)s)".format(key),
                           {'vals': list(map(str, values))}, order_by=order_by)
