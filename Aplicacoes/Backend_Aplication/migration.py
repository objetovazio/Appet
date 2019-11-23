from playhouse.migrate import *

data_base = PostgresqlDatabase('eqvhegcr',
                                      user='eqvhegcr',
                                      password='uOr1RvzMuCvjqpnSPqvadvOnBwZP5oNd',
                                      host='motty.db.elephantsql.com', port=5432)
migrator = PostgresqlMigrator(data_base)

is_deleted = CharField(null = True)
migrate(
    migrator.add_column('usuario','google_id',is_deleted),
)