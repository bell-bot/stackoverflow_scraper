def given_simple_html():
    return """<!DOCTYPE html>
                    <html>
                        <body>

                            <div id="question-header" class="d-flex sm:fd-column">
                                <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1">
                                    <a href="/questions/1373164/how-do-i-create-variable-variables" class="question-hyperlink">How do I python?</a>
                                </h1>
                                <div class="ml12 aside-cta flex--item print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                                    <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
                                        Ask Question
                                    </a>
                                </div>
                            </div>

                            <div class="s-prose js-post-body" itemprop="text">
                
                                <p>I know that some other languages, <a href="https://www.php.net/manual/en/language.variables.variable.php" rel="noreferrer">such as PHP</a>, support a concept of "variable variable names" - that is, the contents of a string can be used as part of a variable name.</p>
                                <p>I heard that this is a bad idea in general, but I think it would solve some problems I have in my Python code.</p>
                                <p>Is it possible to do something like this in Python? What can go wrong?</p>
                                <hr>
                                <p><sub>If you are just trying to <em>look up an existing</em> variable by its name, see <a href="https://stackoverflow.com/questions/47496415">How can I select a variable by (string) name?</a>. However, first consider whether you can reorganize t<div class="s-prose js-post-body" itemprop="text">
                                                
                                <p>I know that some other languages, <a href="https://www.php.net/manual/en/language.variables.variable.php" rel="noreferrer">such as PHP</a>, support a concept of "variable variable names" - that is, the contents of a string can be used as part of a variable name.</p>
                                <p>I heard that this is a bad idea in general, but I think it would solve some problems I have in my Python code.</p>
                                <p>Is it possible to do something like this in Python? What can go wrong?</p>
                                <hr>
                                <p><sub>If you are just trying to <em>look up an existing</em> variable by its name, see <a href="https://stackoverflow.com/questions/47496415">How can I select a variable by (string) name?</a>. However, first consider whether you can reorganize the code to avoid that need, following the advice in this question.</sub></p>
                            </div>he code to avoid that need, following the advice in this question.</sub></p>
                            </div>

                        </body>
                    </html>"""


def given_html_with_complex_header():
    return """<!DOCTYPE html>
                    <html>
                        <body>

                            <div id="question-header" class="d-flex sm:fd-column">
                                <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1">
                                    <a href="/questions/1373164/how-do-i-create-variable-variables" class="question-hyperlink">This <> is a super complex HEADER || since it contains {} signs</a>
                                </h1>
                                <div class="ml12 aside-cta flex--item print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                                    <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
                                        Ask Question
                                    </a>
                                </div>
                            </div>

                            <p>My first paragraph.</p>

                        </body>
                    </html>"""


def given_html_without_header():
    return """<!DOCTYPE html>
                    <html>
                        <body>

                            <div id="question-header" class="d-flex sm:fd-column">
                                <h1 itemprop="NOT A HEADER" class="fs-headline1 ow-break-word mb8 flex--item fl1">
                                    <a href="/questions/1373164/how-do-i-create-variable-variables" class="question-hyperlink">How do I python?</a>
                                </h1>
                                <div class="ml12 aside-cta flex--item print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                                    <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
                                        Ask Question
                                    </a>
                                </div>
                            </div>

                            <p>My first paragraph.</p>

                        </body>
                    </html>"""
