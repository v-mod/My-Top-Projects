try:
    import AriaCore as Aria
    import AriaCore
except:
    print('-> Error in import')
    install = input('Install (Y/N)')
    if install.lower() == 'y':
        print('-> Prepping to install system requirement: Please remember to use python 3.6')
        import AriaInstaller
        AriaInstaller.install()
    else:
        quit()

def main():
    UName= 'Vivaan'
    Aria.sayHi(UName)
    Aria.Aria('Aria')

if __name__=='__main__':
    main()
