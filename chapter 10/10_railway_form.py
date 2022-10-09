class RailwayForm: #class names are usually written using Pascal Case

    formType = "RailwayForm"
    def printData(self):
        print(f'name is {self.name}')
        print(f'train is {self.train}')

shivasApplication = RailwayForm()
shivasApplication.name = "Shivanand"
shivasApplication.train = "Golgumbaz Express"
shivasApplication.printData() 