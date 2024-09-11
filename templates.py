PYTHON_BASE_TEMPLATE='''
client = AsyncConvaAI(
    assistant_id="{assistant_id}", 
    assistant_version="LATEST", # this is a special tag to indicate 
                                # the latest version of the Assistant
    api_key="{api_key}"
        
)
query = "{chosen_query}"
response = asyncio.run(client.invoke_capability(query, stream = False))
message = response.message
parameters = response.parameters
'''



ANDROID_BASE_TEMPLATE='''
ConvaAI.init(
    id = "{assistant_id}",
    key = "{api_key}",
    version = "LATEST", // this is a special tag to indicate 
                        // the latest version of the Assistant
    application = applicationContext
);
val query = "{chosen_query}"
val response = ConvaAI.invokeCapability(input = query);
val message = response.message;
val params = response.params;
'''


FLUTTER_BASE_TEMPLATE='''
ConvaAI.init(
    id: "{assistant_id}",
    key: "{api_key}", 
    version = "LATEST", // this is a special tag to indicate 
                        // the latest version of the Assistant
);
var query = "{chosen_query}"
Response response = await ConvaAI.invokeCapability(input: query);
String message = response.message;
var params = response.params;
'''


IOS_BASE_TEMPLATE='''
ConvaAI.initialize(
    with: "{assistant_id}", 
    key: "{api_key}", 
    version: "LATEST" // this is a special tag to indicate 
                      // the latest version of the Assistant
)
let query = "{chosen_query}"
let response: ConvaAICapability? = try await ConvaAI.invokeCapability(
    with: query
)
let message = response.message
let params = response.params
'''

PYTHON_IF_SYNTAX= "if response.capability == '{capability_name}':\n"
PYTHON_ELIF_SYNTAX = "elif response.capability == '{capability_name}':\n"
PYTHON_COMMENT_SYNTAX = '\t# Use the parameters and handle the "{capability_name}" action\n'
PYTHON_END_SYNTAX = ''

BLOCK_IF_SYNTAX='if (response.capability == "{capability_name}") {{\n'
BLOCK_ELIF_SYNTAX='}} else if (response.capability == "{capability_name}") {{\n'
BLOCK_COMMENT_SYNTAX = '\t// Use the parameters and handle the "{capability_name}" action\n'
BLOCK_END_SYNTAX = '}'


BASE_TEMPLATE_MAP = {
    'python': PYTHON_BASE_TEMPLATE,
    'android': ANDROID_BASE_TEMPLATE,
    'flutter': FLUTTER_BASE_TEMPLATE,
    'ios': IOS_BASE_TEMPLATE
}

IF_SYNTAX_MAP = {
    'python': PYTHON_IF_SYNTAX,
    'android': BLOCK_IF_SYNTAX,
    'flutter': BLOCK_IF_SYNTAX,
    'ios': BLOCK_IF_SYNTAX
}
ELIF_SYNTAX_MAP = {
    'python': PYTHON_ELIF_SYNTAX,
    'android': BLOCK_ELIF_SYNTAX,
    'flutter': BLOCK_ELIF_SYNTAX,
    'ios': BLOCK_ELIF_SYNTAX
}

COMMENT_SYNTAX_MAP = {
    'python': PYTHON_COMMENT_SYNTAX,
    'android': BLOCK_COMMENT_SYNTAX,
    'flutter': BLOCK_COMMENT_SYNTAX,
    'ios': BLOCK_COMMENT_SYNTAX
}


END_SYNTAX_MAP = {
    'python': PYTHON_END_SYNTAX,
    'android': BLOCK_END_SYNTAX,
    'flutter': BLOCK_END_SYNTAX,
    'ios': BLOCK_END_SYNTAX
}