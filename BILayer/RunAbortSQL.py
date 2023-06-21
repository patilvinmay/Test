a
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import snowflake.connector as snowflake
import pandas as pd

# Snowflake credentials
SNOWFLAKE_USER = '<your_snowflake_username>'
SNOWFLAKE_PASSWORD = '<your_snowflake_password>'
SNOWFLAKE_ACCOUNT = '<your_snowflake_account>'
SNOWFLAKE_DATABASE = '<your_snowflake_database>'
SNOWFLAKE_SCHEMA = '<your_snowflake_schema>'
SNOWFLAKE_WAREHOUSE = '<your_snowflake_warehouse>'

class QueryRunner(QThread):
    finished = pyqtSignal()

    def __init__(self, query):
        super().__init__()
        self.query = query
        self.results = None
        self.error = None

    def run(self):
        try:
            # Connect to Snowflake
            conn = snowflake.connect(
                user=SNOWFLAKE_USER,
                password=SNOWFLAKE_PASSWORD,
                account=SNOWFLAKE_ACCOUNT,
                warehouse=SNOWFLAKE_WAREHOUSE,
                database=SNOWFLAKE_DATABASE,
                schema=SNOWFLAKE_SCHEMA
            )

            # Execute the query
            self.cursor = conn.cursor()
            self.cursor.execute(self.query)

            # Fetch the results
            self.results = self.cursor.fetchall()

        except snowflake.connector.errors.ProgrammingError as e:
            # Handle any errors that occur during execution
            self.error = str(e)

        finally:
            if self.cursor:
                self.cursor.close()

            if conn:
                conn.close()

            self.finished.emit()

    def abort(self):
        if self.cursor:
            self.cursor.close()
        self.error = "Query aborted by user"
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snowflake Query Runner')

        self.query_runner = None

        self.run_button = QPushButton('Run', self)
        self.run_button.clicked.connect(self.run_query)
        self.run_button.setGeometry(50, 50, 100, 30)

        self.abort_button = QPushButton('Abort', self)
        self.abort_button.clicked.connect(self.abort_query)
        self.abort_button.setGeometry(160, 50, 100, 30)
        self.abort_button.setEnabled(False)

    def run_query(self):
        self.query_runner = QueryRunner('SELECT * FROM your_table')
        self.query_runner.finished.connect(self.query_finished)
        self.query_runner.start()

        self.run_button.setEnabled(False)
        self.abort_button.setEnabled(True)

    def abort_query(self):
        if self.query_runner:
            self.query_runner.abort()

    def query_finished(self):
        if self.query_runner.error:
            QMessageBox.critical(self, 'Error', self.query_runner.error)
        else:
            df = pd.DataFrame(self.query_runner.results)
            # Do something with the results

        self.run_button.setEnabled(True)
        self.abort_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
