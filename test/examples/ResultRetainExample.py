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

# tag::result-retain-import[]
from neo4j.v1 import GraphDatabase
# end::result-retain-import[]

class ResultRetainExample(BaseApplication):
    def __init__(self, uri, user, password):
        super( uri, user, password );

    # tag::result-retain[]
    def addEmployees(self, companyName):
        try ( Session session = self._driver.session() )
        {
            int employees = 0;
            List<Record> persons = session.readTransaction( new TransactionWork<List<Record>>()
            {
                @Override
                public List<Record> execute( Transaction tx )
                {
                    return matchPersonNodes( tx );
                }
            } );
            for ( final Record person : persons )
            {
                employees += session.writeTransaction( new TransactionWork<Integer>()
                {
                    @Override
                    public Integer execute( Transaction tx )
                    {
                        tx.run( "MATCH (emp:Person {name: $person_name}) " +
                                "MERGE (com:Company {name: $company_name}) " +
                                "MERGE (emp)-[:WORKS_FOR]->(com)",
                                parameters( "person_name", person.get( "name" ).asString(), "company_name",
                                        companyName ) );
                        return 1;
                    }
                } );
            }
            return employees;

    def matchPersonNodes(self, tx):
        return list(tx.run( "MATCH (a:Person) RETURN a.name AS name" ));
    # end::result-retain[]
