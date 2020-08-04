#Error Handling
class OutputTransformer:
    def error_handling_transformer(self):
        result={"Status_code":500,"Message":"Weather API is not responding or city is not available.. check documentation for more details!"}
        return result