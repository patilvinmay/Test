import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import snowflake.connector as snowflake

# Snowflake credentials
SNOWFLAKE_USER = '<your_snowflake_username>'
SNOWFLAKE_PASSWORD = '<your_snowflake_password>'
SNOWFLAKE_ACCOUNT = '<your_snowflake_account>'
SNOWFLAKE_DATABASE = '<your_snowflake_database>'
SNOWFLAKE_SCHEMA = '<your_snowflake_schema>'
SNOWFLAKE_WAREHOUSE = '<your_snowflake_warehouse>'

class QueryWorker(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    results = pyqtSignal(list)

    def __init__(self, query):
        super().__init__()
        self.query = query
        self.running = True

    def run(self):
        try:
            # Connect to Snowflake
            conn = snowflake.connect(
                user=SNOWFLAKE_USER,
                password=SNOWFLAKE_PASSWORD,
                account=SNOWFLAKE_ACCOUNT,
                database=SNOWFLAKE_DATABASE,
                schema=SNOWFLAKE_SCHEMA,
                warehouse=SNOWFLAKE_WAREHOUSE
            )

            # Execute the query asynchronously
            cursor = conn.cursor()
            cursor.execute(self.query, _async=True)

            # Monitor the execution progress
            while cursor.is_still_running():
                if not self.running:
                    cursor.cancel()
                    self.error.emit("Query aborted by user")
                    break

            # Check if the query execution was successful
            if cursor.is_successful():
                # Fetch the results
                results = cursor.fetchall()
                self.results.emit(results)
            else:
                self.error.emit("Query execution failed")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except snowflake.connector.errors.ProgrammingError as e:
            self.error.emit(str(e))

        self.finished.emit()

    def abort(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snowflake Query Executor')

        self.query_worker = None

        self.run_button = QPushButton('Run Query', self)
        self.run_button.clicked.connect(self.run_query)
        self.run_button.setGeometry(50, 50, 100, 30)

        self.abort_button = QPushButton('Abort Query', self)
        self.abort_button.clicked.connect(self.abort_query)
        self.abort_button.setGeometry(160, 50, 100, 30)
        self.abort_button.setEnabled(False)

    def run_query(self):
        query = 'SELECT * FROM your_table'
        self.query_worker = QueryWorker(query)
        self.query_worker.finished.connect(self.query_finished)
        self.query_worker.error.connect(self.query_error)
        self.query_worker.results.connect(self.query_results)
        self.query_worker.start()

        self.run_button.setEnabled(False)
        self.abort_button.setEnabled(True)

    def abort_query(self):
        if self.query_worker:
            self.query_worker.abort()

    def query_finished(self):
        self.run_button.setEnabled(True)
        self.abort_button.setEnabled(False)

    def query_error(self, error):
        QMessageBox.critical(self, 'Error', error)

    def query_results(self, results):
        # Process and display the results
        print(results)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
