from typing import Optional

from metagpt.actions import Action
from metagpt.utils.common import OutputParser, awrite
from metagpt.utils.jscst import merge_jsdoc

JSDOC_SYSTEM = """### Requirements
1. Add JsDoc to the given code.
2. Replace the function body with an Ellipsis object (...).
3. If the types are already annotated, there is no need to include them in the JsDoc.
4. Extract only class, function, or the JsDoc for the module parts from the given JavaScript or TypeScript code, avoiding any other text.

### Input Example
javascript
function function_with_type_annotations(param1) {{
    return typeof param1 === 'number';
}}

class ExampleError {{
    constructor(msg) {{
        this.msg = msg;
    }}
}}

### Output Example
javascript
{example}
"""

JSDOC_EXAMPLE = '''
/**
 * Example function with type annotations.
 *
 * @param {number} param1 - The first parameter.
 * @returns {boolean} The return value. True for success, False otherwise.
 */
function function_with_type_annotations(param1) {
    ...
}

/**
 * Exceptions are documented in the same way as classes.
 *
 * @param {string} msg - Human readable string describing the exception.
 */
class ExampleError {
    constructor(msg) {
        ...
    }
}
'''

class WriteJsDoc(Action):
    """This class is used to write JsDoc for code.

    Attributes:
        desc: A string describing the action.
    """

    desc: str = "Write JsDoc for code."
    i_context: Optional[str] = None

    async def run(
            self,
            code: str,
            system_text: str = JSDOC_SYSTEM,
    ) -> str:
        """Writes JsDoc for the given code and system text.

        Args:
            code: A string of JavaScript or TypeScript code.
            system_text: A string of system text.

        Returns:
            The JavaScript or TypeScript code with JsDoc added.
        """
        system_text = system_text.format(example=JSDOC_EXAMPLE.strip())
        documented_code = await self._aask(f"javascript\n{code}\n", [system_text])
        documented_code = OutputParser.parse_jscode(documented_code)
        return merge_jsdoc(code, documented_code)

    @staticmethod
    async def write_jsdoc(code_files, output_dir):
        wrt_dcs = WriteJsDoc(desc="Write JsDoc for code by also taking the main ideas behind the code into account.")
        for file_name, item in code_files.items():
            code = await wrt_dcs.run((item["content"]))
            await awrite(f"{output_dir}/{item['path']}", code)
            print(code)