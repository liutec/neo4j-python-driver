#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2017 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# tag::cypher-error-import[]
from neo4j.v1 import GraphDatabase
# end::cypher-error-import[]

class CypherErrorExample(BaseApplication):
    def __init__(uri, user, password):
        super(uri, user, password)

    # tag::cypher-error[]
    def getEmployeeNumber(self, name):
        session = self._driver.session()
        {
            return session.readTransaction( new TransactionWork<Integer>()
            {
                @Override
                public Integer execute( Transaction tx )
                {
                    return selectEmployee( tx, name );
                }
            } );
        }
    }

    def selectEmployee(self, tx, name):
        try
        {
            StatementResult result = tx.run( "SELECT * FROM Employees WHERE name = $name", parameters( "name", name ) );
            return result.single().get( "employee_number" ).asInt();
        }
        catch ( ClientException ex )
        {
            System.err.println( ex.getMessage() );
            return -1;
        }
    # end::cypher-error[]
