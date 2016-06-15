from stock_tracer.library import transaction
from stock_tracer.model import Stock
from stock_tracer.operation.base import Base

class AddStockOperation(Base):
    """AddStockOperation"""
    def __init__(self, exchange, symbol, *args, **kwargs):
        """__init__

        :param exchange:
        :param symbol:
        :param *args:
        :param **kwargs:
        """
        super(AddStockOperation, self).__init__(*args, **kwargs)
        self.exchange = exchange
        self.symbol = symbol

    def execute(self):
        """execute the operation"""
        with transaction(self.env) as tx:
            stock = Stock(exchange=self.exchange, symbol=self.symbol)
            tx.add(stock)