import click

from core.extensions import db


@click.command("initdb")
@click.option("--drop", is_flag=True, help="先删除再创建所有表")
def initdb(drop):
    """初始化数据库。"""
    if drop:
        click.confirm("⚠️  确认要删除所有数据吗？", abort=True)
        db.drop_all()
        click.echo("✔️  已删除所有表。")
    db.create_all()
    click.echo("✔️  数据库初始化完毕。")
