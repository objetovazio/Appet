from playhouse.migrate import *

data_base = PostgresqlDatabase('eqvhegcr',
                                      user='eqvhegcr',
                                      password='uOr1RvzMuCvjqpnSPqvadvOnBwZP5oNd',
                                      host='motty.db.elephantsql.com', port=5432)
migrator = PostgresqlMigrator(data_base)

is_deleted = IntegerField(default=0)
migrate(
    migrator.add_column('servico','is_deleted',is_deleted),
    migrator.add_column('horarioservico','is_deleted',is_deleted),
)