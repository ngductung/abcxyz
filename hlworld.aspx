<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="HelloWorld.aspx.cs" Inherits="YourNamespace.HelloWorld" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Hello World</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h1>
                <% Response.Write("Hello, World!"); %>
            </h1>
        </div>
    </form>
</body>
</html>
