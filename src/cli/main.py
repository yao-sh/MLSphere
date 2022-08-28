import os
import json
import typer
from loguru import logger
from typing import Optional
from mlbox.src.pkg.builder import Builder
from mlbox.src.pkg.runner import Runner

app = typer.Typer()

@app.command()
def build(src_path: Optional[str] = './'):
    """
    Build the image from mlsphere.json
    """
    src_path = os.path.join(src_path, "mlsphere.json")
    logger.info(f"Source Code Path: {src_path}")
    
    with open(src_path, 'r') as fp:
        config = json.load(fp)
    
    builder = Builder()
    builder.build(config)


@app.command()
def run(src_path: Optional[str] = './'):
    """
    Run a specific command defined in mlsphere.json
    """
    src_path = os.path.join(src_path, "mlsphere.json")
    logger.info(f"Source Code Path: {src_path}")
    with open(src_path, 'r') as fp:
        config = json.load(fp)
    runner = Runner()
    runner.run_command(config)

@app.command()
def run_pipeline(src_path: Optional[str] = './'):
    """
    Run the pipeline defined in mlsphere.json
    """
    logger.info(f"Source Code Path: {src_path}")
    with open(src_path, 'r') as fp:
        config = json.load(fp)
    builder = Builder()
    builder.build(config)

if __name__ == "__main__":
    app()
