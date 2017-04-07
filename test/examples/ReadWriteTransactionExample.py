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

# tag::read-write-transaction-import[]
from neo4j.v1 import GraphDatabase
# end::read-write-transaction-import[]

class ReadWriteTransactionExample(BaseApplication):
    def __init__(self, uri, user, password):
        super(uri, user, password)

    # tag::read-write-transaction[]
    def addPerson(self, name):
        try ( Session session = driver.session() )
        {
            session.writeTransaction( new TransactionWork<Void>()
            {
                @Override
                public Void execute( Transaction tx )
                {
                    return createPersonNode( tx, name );
                }
            } );
            return session.readTransaction( new TransactionWork<Long>()
            {
                @Override
                public Long execute( Transaction tx )
                {
                    return matchPersonNode( tx, name );
                }
            } );
        }
    }

    def createPersonNode(self, tx, name):
        tx.run("CREATE (a:Person {name: $name})", { "name": name })
        return None;

    def matchPersonNode(self, tx, name):
        result = tx.run( "MATCH (a:Person {name: $name}) RETURN id(a)", {"name": name })
        return result.single().get( 0 ).asLong()
    # end::read-write-transaction[]
