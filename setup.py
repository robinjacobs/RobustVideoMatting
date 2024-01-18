from setuptools import setup
setup(
    name='robustmatting',
    version='0.1.0',
    install_requires=['av>=8.0.3',
            'torch>=2.0.0',
            'torchvision>=0.10.0',
            'tqdm==4.61.1',
            'pims==0.5'],
    description='Robust Matting'
)
