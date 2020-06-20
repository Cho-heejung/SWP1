html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                a = <input type = "number" name = "a">
            </p>
            <p>
                b = <input type = "number" name = "b">
            </p>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
        <p>
            Sum: %(sum)s</br>
            Product: %(product)s</br>
        </p>
    </body>
</html>
"""
