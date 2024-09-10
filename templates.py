PYTHON_BASE_TEMPLATE='''
client = AsyncConvaAI(
    assistant_id="{assistant_id}", 
    assistant_version="LATEST", # this is a special tag to indicate 
                            # the latest version of the Assistant
    api_key="{api_key}"
        
)
response = await client.invoke_capability("<user_input>")
message = response.message
'''

PYTHON_PARAM_TEMPLATE = "{param_name} = response.parameters['{param_name}']\n"

ANDROID_BASE_TEMPLATE='''
ConvaAI.init(
    id = "{assistant_id}",
    key = "{api_key}",
    version = "LATEST", // this is a special tag to indicate 
                        // the latest version of the Assistant
    application = applicationContext
);
val response = ConvaAI.invokeCapability(input = "<user_input>")
val message = response.message
'''
ANDROID_PARAM_TEMPLATE='val {param_name} = response.params["{param_name}"]\n'

FLUTTER_BASE_TEMPLATE='''
ConvaAI.init(
    id: "{assistant_id}",
    key: "{api_key}", 
    version = "LATEST", // this is a special tag to indicate 
                        // the latest version of the Assistant
);
Response response = await ConvaAI.invokeCapability(input: "<user_input>");
String message = response.message;


'''
FLUTTER_PARAM_TEMPLATE="var {param_name} = response.params['{param_name}'];\n"


IOS_BASE_TEMPLATE='''
ConvaAI.initialize(
    with: "{assistant_id}", 
    key: "{api_key}", 
    version: "LATEST" // this is a special tag to indicate 
                      // the latest version of the Assistant
)
let response: ConvaAICapability? = try await ConvaAI.invokeCapability(
    with: "<user_input>"
)
let message = response.message
'''
IOS_PARAM_TEMPLATE='let {param_name} = response.params["{param_name}"]\n'




BASE_TEMPLATE_MAP = {
    'python': PYTHON_BASE_TEMPLATE,
    'android': ANDROID_BASE_TEMPLATE,
    'flutter': FLUTTER_BASE_TEMPLATE,
    'ios': IOS_BASE_TEMPLATE
}

PARAM_TEMPLATE_MAP = {
    'python': PYTHON_PARAM_TEMPLATE,
    'android': ANDROID_PARAM_TEMPLATE,
    'flutter': FLUTTER_PARAM_TEMPLATE,
    'ios': IOS_PARAM_TEMPLATE
}