# John Burnson
# CSC505
# Module 2

class Burnson:
    def __init__(self, flow_title):
        self.flow_title = flow_title
        self.flow_stages = []   # List of class WaterfallStages
        
    def fill_stages(self):
        input_stages = input("List the stages in sequence, separated by ' -> '")
        for input_stage_name in input_stages.split(' -> '):
            self.add_stage(WaterfallStage(input_stage_name))
        print('')

    def add_stage(self, flow_stage):
        self.flow_stages.append(flow_stage)

    def print_flow(self):
        print(self.flow_title)
        # Print stage names
        print("---> ".join(obj.stage_name.ljust(25) for obj in self.flow_stages))
        print("     ".join(('=' * 25).ljust(25) for obj in self.flow_stages))
        # Get size of longest list of steps
        max_steps_in_stage = max([len(i.stage_steps) for i in self.flow_stages])
        # Print lines of step names, 1 by 1
        for i in range(max_steps_in_stage):
            step_string = ""
            for obj in self.flow_stages:
                try:
                    step_string = step_string + obj.stage_steps[i].step_name.ljust(30)
                except IndexError:
                    step_string = step_string + ' ' * 30
            print(step_string)

class WaterfallStage:
    def __init__(self, stage_name):
        self.stage_name = stage_name
        self.stage_steps = []   # List of class WaterfallSteps

    def fill_steps(self):
        print('STAGE:', self.stage_name)
        input_steps = input()
        for input_step_name in input_steps.split(' / '):
            self.add_step(WaterfallStep(input_step_name))

    def add_step(self, stage_step):
        self.stage_steps.append(stage_step)

    def print_stage(self):  # Dubious
        for index, value in enumerate(self.stage_steps):
            print()

class WaterfallStep:
    def __init__(self, step_name):
        self.step_name = step_name

    def print_step(self):  # Dubious
        pass # print(self.step_name)

def main():
    print("\n*** Main Start ***\n")

    # Instantiate the flow
    burnson_model = Burnson('Burnson Waterfall Model')

    # Get the stages within the flow
    burnson_model.fill_stages()

    # Get the steps within each stage
    print("List the steps in each stage, separated by ' / '")
    for index, value in enumerate(burnson_model.flow_stages): 
        value.fill_steps()
    print()

    # Display the flow
    burnson_model.print_flow()

    print("\n*** Main End ***\n")

if __name__ != "__main__":
    print('This program is being imported from another module, so do not run main().')
else:
    print('This program is being executed as __main__')
    main()