class HtmlText:
    def __init__(self, text: str):
        self.text = str(text)
        self.tags = []

    def _add_tag(self, tag: str):
        self.tags.append(tag)
        return self

    def div(self):
        return self._add_tag("div")

    def p(self):
        return self._add_tag("p")

    def i(self):
        return self._add_tag("i")

    def h1(self):
        return self._add_tag("h1")

    def render(self) -> str:
        opening = "".join(f"<{tag}>" for tag in self.tags)
        closing = "".join(f"</{tag}>" for tag in reversed(self.tags))
        return f"{opening}{self.text}{closing}"

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()


s1 = HtmlText("test1")
print(s1.div().h1())  # <div><h1>test1</h1></div>

s2 = HtmlText("test2")
print(s2.div().p().h1())  # <div><p><h1>test2</h1></p></div>

head = HtmlText("Title")
print(head.h1().i())  # <h1><i>Title</i></h1>