# (C) Copyright 2023 Beijing Academy of Quantum Information Sciences
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Interface provider."""


# pylint: disable=too-few-public-methods
class InterfaceProvider:
    _init = False
    _providers = {}

    @classmethod
    def get(cls, name: str):
        if not cls._init:
            # pylint: disable=import-outside-toplevel
            from .interface.torch import TorchTransformer

            cls._providers["torch"] = TorchTransformer

            cls._init = True

        if name not in cls._providers:
            raise NotImplementedError(f"Unsupported interface: {name}")
        return cls._providers[name]
