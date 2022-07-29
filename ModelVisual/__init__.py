from tensorflow.keras.models import Sequential, Model
import tensorflow as tf

class ModelVisual:

    def __init__(self, model, name: str = 'ModelVisual.html', path: str = '',chart_fill_color: str = '#398AB9', chart_stroke_color: str = '#398AB9', chart_stroke_width: int = 3):
        self.model = model
        self.name = name
        self.path = path
        self.chart_fill_color = chart_fill_color
        self.chart_stroke_color = chart_stroke_color
        self.chart_stroke_width = chart_stroke_width
        self.flowchart_codes = []
        self.nodes = []

        self.div_code_template = 'flowchart TD;classDef default fill:{fill_color},stroke:{stroke_color},stroke-width:{strole_width}px;'
        self.div_code = ''
        self.fullCode_template = '''
        <!DOCTYPE html>
        <html>
            <body>
                <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
                <script>
                    mermaid.initialize({startOnLoad_true});
                </script>

                <div class="mermaid">
                    {div_code}
                </div>
            </body>
        </html>
        '''
    
    def set_name(self, name: str):

        self.name = name
    
    def set_path(self, path: str):

        self.path = path
    
    def set_chart_fill_color(self, chart_fill_color: str):

        self.chart_fill_color = chart_fill_color
    
    def set_chart_stroke_color(self, chart_stroke_color: str):

        self.chart_stroke_color = chart_stroke_color
    
    def set_chart_stroke_width(self, chart_stroke_width: int):

        self.chart_stroke_width = chart_stroke_width
    
    def set_model(self, model):

        self.model = model
    
    # tools ---------------------------------------------------------------------------------------------------------------------

    # check if layer's input is empty,if so, get the tail of the list and set it as the input
    def get_head_and_tail(self, _nodes):

        head = []
        tail = []
        for i in range(len(_nodes)):
            if _nodes[i][2] == _nodes[i][0]:
                head.append(_nodes[i][2])
            if _nodes[i][0] not in [r[2] for r in _nodes]:
                tail.append(_nodes[i][0])
        return head,tail

    def get_outputShape(self, nodes: list,layer: str):

        outputShape = []
        for i in range(len(nodes)):
            if nodes[i][0] == layer:
                return str(nodes[i][1]).replace('(', '').replace(')', '').replace(' ', '')

    def flowchart_conn(self,name_1: str,shape_1: str,name_2: str,shape_2: str):

        self.flowchart_codes.append(name_1+r'\n'+shape_1+' --- '+name_2+r'\n'+shape_2)

    # generate ---------------------------------------------------------------------------------------------------------------------

    def get_nodes(self):

        nodes = []
        for i in range(len(self.model.layers)):
            nodes.append([0,0,'empty'])
            nodes[i][0] = self.model.layers[i].name    # get layer names
            nodes[i][1] = self.model.layers[i].output_shape    # get layer shapes

            # some time the shape is a list, so we need to convert 
            if type(nodes[i][1]) == list:
                nodes[i][1] = nodes[i][1][0]   
            try:
                a,b,c = str(self.model.layers[i].input.name).partition('/')
                if '_input' in a: # sometimes the layer name includes _input, we need to remove it
                    a = a.replace('_input','')
                nodes[i][2] = a    # get layer input names
            except:
                # if the layer has no input(maybe it is concatenate), it will be an error
                pass

        _nodes = nodes.copy()
        for i in range(len(_nodes)):
            if nodes[i][2] == 'empty':
                del _nodes[i:]
                nodes[i][2] = self.get_head_and_tail(_nodes)[1]
        
        self.nodes = nodes
    
    def run(self):

        self.get_nodes()
        for i in range(len(self.nodes)):
            if self.nodes[i][2] == self.nodes[i][0]:
                pass
            else:
                try:
                    self.flowchart_conn(self.nodes[i][2],self.get_outputShape(self.nodes,self.nodes[i][2]),self.nodes[i][0],self.get_outputShape(self.nodes,self.nodes[i][0]))
                except:
                    for r in self.nodes[i][2]:
                        r = str(r)
                        self.flowchart_conn(r,self.get_outputShape(self.nodes,r),self.nodes[i][0],self.get_outputShape(self.nodes,self.nodes[i][0]))

        self.div_code = ';'.join(self.flowchart_codes)
        self.div_code = self.div_code_template.format(fill_color=self.chart_fill_color,stroke_color=self.chart_stroke_color,strole_width=self.chart_stroke_width) + self.div_code
        self.fullCode = self.fullCode_template.format(startOnLoad_true='''startOnLoad: true''',div_code=self.div_code)

    # save ---------------------------------------------------------------------------------------------------------------------

    def return_web_page(self):

        return self.fullCode
    
    def save_web_page(self):

        with open(self.path+self.name, 'w') as f:
            f.write(self.fullCode)

    def return_js_code(self):

        return self.div_code
        